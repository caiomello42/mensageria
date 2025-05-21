# Importa módulos para manipular JSON, conectar ao RabbitMQ e pausar execução
import json, pika, time


# Função que será chamada para processar mensagens recebidas na fila
def update_student(ch, method, properties, body):
    # Converte o corpo da mensagem JSON para um dicionário Python
    data = json.loads(body)
    # Extrai nome e email do aluno do dicionário
    name = data.get('name')
    email = data.get('email')
    # Define o status do aluno como 'concluído'
    status = 'concluído'
    # Simula um processamento que leva 2 segundos (ex: atualizar dados no banco)
    time.sleep(2)
    # Imprime no console que o aluno foi atualizado com o status
    print(f'Aluno atualizado: {name} - {email} - {status}')
    # Envia confirmação (ACK) para o RabbitMQ, indicando que a mensagem foi processada
    ch.basic_ack(delivery_tag=method.delivery_tag)


# Bloco principal do script
if __name__ == '__main__':
    # Cria conexão com RabbitMQ rodando no localhost
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    # Abre um canal para enviar/receber mensagens
    channel = connection.channel()

    # Configura o consumidor para escutar a fila 'update_student'
    # e chamar a função 'update_student' quando uma mensagem chegar
    channel.basic_consume(
        queue='update_student',
        on_message_callback=update_student,
    )

    # Começa a escutar e processar mensagens da fila indefinidamente
    channel.start_consuming()
