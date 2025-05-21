# Importa módulos para manipulação de JSON, conexão com RabbitMQ e controle de tempo
import json, pika, time


# Função callback que será executada quando chegar uma mensagem na fila
def send_notification(ch, method, properties, body):
    # Decodifica a mensagem JSON para um dicionário Python
    data = json.loads(body)
    # Extrai o nome e email do dicionário
    name = data.get('name')
    email = data.get('email')
    
    # Simula um processo que demora 3 segundos (exemplo: envio de notificação)
    time.sleep(3)
    
    # Imprime no console que a notificação foi enviada para aquela pessoa
    print(f'Notificação enviada: {name} - {email}')
    
    # Envia confirmação para o RabbitMQ que a mensagem foi processada (ACK)
    ch.basic_ack(delivery_tag=method.delivery_tag)


# Bloco principal do script
if __name__ == '__main__':
    # Estabelece conexão com o RabbitMQ no host local
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    # Cria um canal para comunicação com o RabbitMQ
    channel = connection.channel()

    # Configura o consumidor para escutar a fila 'send_notification' e usar a função callback
    channel.basic_consume(
        queue='send_notification',           # Nome da fila a ser consumida
        on_message_callback=send_notification,  # Função chamada para processar a mensagem
    )

    # Inicia o loop para ficar escutando mensagens na fila e processá-las assim que chegarem
    channel.start_consuming()
