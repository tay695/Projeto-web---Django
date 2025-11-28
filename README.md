🌱 SoliBank

O SoliBank é uma plataforma web desenvolvida para facilitar o gerenciamento de doações, oferecendo um fluxo claro entre doadores, estoque interno e entidades beneficiadas.
O sistema organiza todo o processo: desde o envio da doação, passando pela coleta, até sua destinação final para famílias e ONGs.

🎯 Objetivo do Sistema

O SoliBank tem como propósito:

Registrar doações realizadas por usuários doadores;

Controlar entradas e saídas de itens no estoque;

Apoiar o trabalho do Assistente Social na organização e distribuição das doações;

Manter histórico e transparência de todas as movimentações.

🧩 Arquitetura do Sistema
1. doador

Módulo responsável pela interação do doador com o sistema.
Funcionalidades:

Cadastro e login;

Envio de doações por formulário;

Informar ponto de coleta;

Acompanhar o status da doação (coletada ou não);

Visualizar histórico e informações permitidas.

2. estoque

Módulo central para o controle das doações recebidas.
Funcionalidades:

Registrar entradas (doações coletadas);

Registrar saídas (destinadas às entidades beneficiadas);

Listar itens e acompanhar quantidades disponíveis.

Fluxo básico do estoque:

Doação enviada → fica pendente

Assistente Social coleta → gera entrada no estoque

3. entidade_beneficiada

Acesso exclusivo para o Assistente Social.
Funcionalidades:

Cadastro de famílias e ONGs beneficiadas;

Atualização, consulta e remoção de registros;

Visualização do histórico de itens recebidos.

4. doacao

App auxiliar que organiza e vincula as doações aos demais módulos.
Funcionalidades:

Registrar todas as doações enviadas pelos usuários;

Controlar status da coleta;

Relacionar doações às movimentações do estoque.

👥 Perfis do Sistema
Assistente Social (Superusuário)

Gerencia entidades beneficiadas;

Controla entradas e saídas do estoque;

Atualiza o status das doações (coletada/não coletada);

Administra a logística interna do sistema.

Doador (Usuário Comum)

Realiza cadastro e login;

Envia doações via formulário;

Informa o ponto de coleta;

Acompanha o status da própria doação;

Acessa apenas funcionalidades relacionadas ao seu perfil.

🔄 Fluxo do Sistema

O doador envia a doação pelo formulário e informa o ponto de coleta.

A doação fica registrada como pendente.

O Assistente Social verifica e atualiza o status da coleta.

Se coletada, gera uma entrada no estoque.

O Assistente Social destina os itens a famílias ou ONGs, registrando uma saída.

Todo o processo fica registrado no histórico do sistema.

🛠️ Instruções de Execução
Pré-requisitos

Python 3.8+

Django 4.x

Git (opcional)

Passos para execução

Clonar o repositório

Aplicar as migrações do Django

Criar um superusuário (Assistente Social)

Executar o servidor:

python manage.py runserver


Acessar no navegador:

http://127.0.0.1:8000


Para mais detalhes sobre comandos, configurações e boas práticas, consulte a documentação oficial do Django:
🔗 https://www.djangoproject.com/

💻 Desenvolvedoras Full Stack

Jéssica Tainá

Maria Clara

Tainara Amaral

🎥 Vídeo de Apresentação do Sistema

(Adicionar link posteriormente.)
