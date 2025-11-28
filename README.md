SoliBank
Objetivo do Sistema
O SoliBank é um sistema web voltado para o gerenciamento de doações, organizando o fluxo entre doadores, estoque interno e entidades beneficiadas (famílias e ONGs).
O objetivo é registrar doações, controlar entradas e saídas no estoque e facilitar o trabalho do assistente social na gestão da logística.

Arquitetura do Sistema 
1. doador
Responsável pela interação do doador com o sistema.
Funções:
Cadastro e login do doador
Envio de doações por formulário
Informar ponto de coleta
Acompanhar o status da doação (coletada ou não)
Visualizar suas doações e informações gerais permitidas

2. estoque

Módulo que controla e armazena os itens doados.
Funções:

Registrar entradas (quando a doação é coletada)

Registrar saídas (quando os itens são destinados a uma entidade beneficiada)

Listar itens e acompanhar quantidades

Fluxo básico:

Doação enviada → status pendente

Assistente Social marca como coletada → gera entrada no estoque

3. entidade_beneficiada

Acesso exclusivo do Assistente Social.
Funções:

Cadastro de famílias e ONGs beneficiadas

Atualização e remoção de registros

Consulta do histórico de itens recebidos

4. doacao

App auxiliar para organização das doações.
Funções:

Registrar a doação enviada pelo doador

Associar a doação às movimentações de estoque

Controlar o status de coleta

Perfis do Sistema
Assistente Social (Superusuário)

Gerencia entidades beneficiadas

Controla entradas e saídas no estoque
Atualiza o status das doações (coletada / não coletada)

Organiza a logística interna do sistema

Doador (Usuário Comum)

Realiza cadastro e login

Envia doações

Informa ponto de coleta

Acompanha a situação da própria doação

Tem acesso somente às funcionalidades destinadas ao doador

Fluxo do Sistema

O doador envia uma doação por meio de um formulário (com possibilidade de se cadastrar no processo).

Informa o ponto de coleta e os detalhes da doação.

A doação fica registrada como pendente de coleta.

O Assistente Social verifica e atualiza o status da doação.

Quando marcada como coletada, a doação gera uma entrada no estoque.

O Assistente Social destina os itens a famílias ou ONGs, registrando uma saída no estoque.

O histórico completo do fluxo fica registrado no sistema.

Instruções de Execução
Pré-requisitos

Python 3.8+

Django 4.x

Git (opcional)

Passos para rodar o projeto

Clonar o repositório

Criar migrações e migrar o banco

Criar um superusuário (perfil de Assistente Social)

Executar o servidor:

python manage.py runserver


Acessar no navegador:

http://127.0.0.1:8000

ṕara melhores informações acesse a documentação oficial do Django https://www.djangoproject.com/

desenvolvedores full stack
Jéssica Tainá
Maria Clara
Tainara Amaral

Vídeo de Apresentação do sitemas
(Adicionar link posteriormente.)
