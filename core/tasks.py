# Importa o decorator para criar tarefas compartilhadas do Celery
from celery import shared_task

# Importa o módulo time para simular atrasos com sleep
import time


# Define uma tarefa assíncrona do Celery para gerar certificado
@shared_task
def generate_certificate(data):
    # Pega o nome da pessoa no dicionário recebido
    name = data.get('name')
    # Pega o email da pessoa
    email = data.get('email')
    # Pega o curso que a pessoa realizou
    course = data.get('course')
    # Simula uma operação demorada (por exemplo, gerar o certificado)
    time.sleep(5)
    # Exibe no console que o certificado foi gerado para aquela pessoa e curso
    print(f'Certificado gerado: {name} - {email} - {course}')


# Define uma tarefa assíncrona para enviar uma notificação
@shared_task
def send_notification(data):
    # Pega o nome e email do dicionário recebido
    name = data.get('name')
    email = data.get('email')
    # Simula um atraso (ex: enviando email)
    time.sleep(3)
    # Exibe no console que a notificação foi enviada para o usuário
    print(f'Notificação enviada: {name} - {email}')


# Define uma tarefa assíncrona para atualizar o status do aluno
@shared_task
def update_student(data):
    # Pega nome e email do aluno
    name = data.get('name')
    email = data.get('email')
    # Define o status do aluno como 'concluído'
    status = 'concluído'
    # Simula um atraso (ex: atualização em banco de dados)
    time.sleep(2)
    # Exibe no console que o aluno foi atualizado com o novo status
    print(f'Aluno atualizado: {name} - {email} - {status}')
