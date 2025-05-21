# Importa o módulo de administração do Django, que permite gerenciar o site admin
from django.contrib import admin

# Importa a função 'path' para definir rotas/URLs no Django
from django.urls import path

# Importa as views do aplicativo atual (que estão definidas no arquivo views.py)
from . import views

# Define as URLs da aplicação
urlpatterns = [
    # URL para acessar o painel administrativo do Django
    path('admin/', admin.site.urls),

    # URL para acessar a API de certificados, que está vinculada à view CertificateView
    # Essa view é baseada em classe (por isso o .as_view()), e está nomeada como 'certificate'
    path('api/v1/certificate/', views.CertificateView.as_view(), name='certificate'),
]
