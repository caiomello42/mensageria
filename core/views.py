# Importa classes para criar views baseadas em API do Django REST Framework
from rest_framework import views, response, status

# Importa as tasks assíncronas definidas com Celery
from .tasks import generate_certificate, send_notification, update_student


# Define uma API View para lidar com requisições relacionadas a certificados
class CertificateView(views.APIView):

    # Método que responde a requisições POST (envio de dados)
    def post(self, request):
        # Pega os dados enviados na requisição (normalmente JSON)
        data = request.data

        # Chama as tasks Celery de forma assíncrona (com .delay), passando os dados recebidos
        # Isso faz as tarefas rodarem em background, não bloqueando a resposta HTTP
        generate_certificate.delay(data)
        send_notification.delay(data)
        update_student.delay(data)

        # Retorna uma resposta JSON com status HTTP 201 (Created)
        # Indicando que o certificado foi gerado e enviado (assumidamente, pois as tasks são async)
        return response.Response(
            data={
                'status': 'ok',
                'message': 'Certificado gerado e enviado.',
                'data': data,  # Retorna os dados recebidos para confirmação
            },
            status=status.HTTP_201_CREATED,
        )
