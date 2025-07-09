# 🚀 **Sistema de Processamento Assíncrono com RabbitMQ e Celery** 🚀

Estou muito feliz em compartilhar a conclusão deste projeto que aborda conceitos fundamentais de processamento assíncrono, mensageria e filas! A aplicação foi desenvolvida utilizando Django, RabbitMQ e Celery, simulando fluxos essenciais de uma aplicação escalável.

---

## 🔄 **Funcionalidades:**

- **Atualização de Status dos Alunos**: Realizada de forma assíncrona, permitindo maior eficiência no processamento de dados 🧑‍💻
- **Processamento em Background**: Utilizando **RabbitMQ** e **Celery**, o sistema processa tarefas de forma eficiente, sem sobrecarregar o servidor 🕹️
- **Comunicação Desacoplada**: Garantindo comunicação entre serviços de forma eficiente e escalável 🔗

---

## 💡 **Tecnologias Utilizadas:**

- **Python** | **Django**: Framework backend para desenvolvimento web 🖥️
- **Django REST Framework**: Para construir APIs RESTful 💻
- **RabbitMQ**: Sistema de mensageria para gerenciar filas de tarefas 📩
- **Celery**: Para realizar o processamento assíncrono de tarefas 🔄
- **Pika**: Cliente RabbitMQ para Python, utilizado para facilitar a comunicação entre os serviços 📡

---

## ⚡ **Como Funciona o Sistema?**

- **Django** gerencia a aplicação web e fornece uma API através do Django REST Framework para atualização de status dos alunos.
- **RabbitMQ** é usado para gerenciar as filas e mensageria entre os processos.
- **Celery** processa as tarefas em segundo plano, permitindo que o sistema seja mais rápido e escalável, sem bloquear a execução de outras tarefas.
- **Pika** serve como cliente para conectar o Django com o RabbitMQ, garantindo a comunicação eficiente.

---

## 🚀 **Destaques do Projeto:**

- **Escalabilidade**: O uso de **RabbitMQ** e **Celery** permite que o sistema seja escalável, processando múltiplas tarefas em paralelo sem impactar a performance 🔝
- **Processamento Assíncrono**: Tarefas como a atualização de status de alunos são processadas em background, sem bloquear o fluxo principal da aplicação 🕹️
- **Arquitetura Desacoplada**: A comunicação entre os serviços é realizada de maneira desacoplada, o que garante maior flexibilidade e manutenção do sistema 🔗

---

## 🌱 **Como Rodar o Projeto:**

1. Clone o repositório:
   ```bash
   git clone https://github.com/caiomello42/mensageria.git
