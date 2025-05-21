# Importa módulos para manipulação de JSON, comunicação com RabbitMQ e controle de tempo
import json, pika, time

# Função callback que será executada ao receber uma mensagem na fila
def generate_certificate(ch, method, properties, body):
    # Decodifica o corpo da mensagem, que vem em JSON, para um dicionário Python
    data = json.loads(body)
    # Extrai as informações do dicionário
    name = data.get('name')
    email = data.get('email')
    course = data.get('course')
    
    # Simula um processamento que demora 5 segundos (ex: gerar certificado)
    time.sleep(5)
    
    # Exibe no console que o certificado foi gerado para os dados recebidos
    print(f'Certificado Gerado com Sucesso: {name} - {email} - {course}')
    
    # Envia um ACK para o RabbitMQ confirmando que a mensagem foi processada com sucesso
    ch.basic_ack(delivery_tag=method.delivery_tag)
    

# Bloco principal do programa
if __name__ == '__main__':
    # Estabelece conexão com o RabbitMQ no host local (localhost)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    # Cria um canal de comunicação para enviar e receber mensagens
    channel = connection.channel()

    # Define o consumidor da fila 'generate_certificate', associando a função de callback
    channel.basic_consume(
        queue='generate_certificate',         # Nome da fila que será consumida
        on_message_callback=generate_certificate,  # Função chamada para processar cada mensagem
    )

    # Inicia o loop de consumo, esperando e processando mensagens da fila indefinidamente
    channel.start_consuming()
