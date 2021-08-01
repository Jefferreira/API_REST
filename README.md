# API_REST

#**Descrição:**

Para execuçação do programa e preciso ter um ambiente virtual instalado.

#**Aluno:**

Jeferson Ferreira Freitas

#**Data:**

01/08/2021

<b>Atenção!!! todos os comandos devem ser executados na pasta raiz do projeto.</b>

## Requisitos

### Preprando o ambiente virtual

Primeiramente, é necessário preparar o ambiente virtual do python. Para isso usaremos o pacote [virtualenv](https://pypi.org/project/virtualenv/)

Com o pacote [virtualenv](https://pypi.org/project/virtualenv/) devidamente instalado, crie e ative um novo ambiente virtual.

### Instalando as dependências
execute `python -m pip install -r requirements.txt`

### Criando as tabelas do banco de dados
execute `python api_rest/manage.py migrate`

### Adicionando registros nas tabelas
aqui vai o comandos para adicionar os registros...

## Testando a aplicação
execute `python api_rest/manage.py runserver`

Acesse o localhost através do seguinte link: http://127.0.0.1:8000/
