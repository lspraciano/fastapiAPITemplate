# FastAPI - API Template

E aí, tudo bem?

Este repositório foi desenvolvido para ser boilerplate de uma API
desenvolvida usando FastAPI. A aplicação deste projeto, por padrão,
é agnóstica de banco de dados com sua arquitetura focada em
"cloud" e "factory". Desta forma poderemos desenvolver diretamente
no docker reduzindo problemas inconvenientes durante o deploy da
aplicação.

No gif abaixo, você pode observar uma das vantagens: mesmo ao executar
no ambiente Docker, a funcionalidade de autoreload permanece ativa.

![autoreload_exemple.gif](autoreload_exemple.gif)

## ☑️ Andamento do Projeto

- Em Desenvolvimento

Este projeto é atualizado periodicamente.

## ☄️ Versão Atual

- 0.1.0

## 🕹️ Estrutura do Projeto

Vamos entender a disposição dos arquivos deste projeto, que foi distribuído
entre os seguintes arquivos e pastas:

1. app
2. configuration
3. docker
4. docs
5. migrations
6. tests
7. .python-version
8. alembic.ini
9. docker-compose.dev.yaml
10. docker-compose.prod.yaml
11. docker-compose.test.yaml
12. poetry.lock
13. pyproject.toml

### 📁 app

Nesta pasta encontramos os arquivos principais da aplicação. Ela
se divide em:

1. 📁 api
2. 📁 core
3. 📁 utils
4. 📋 main.py

#### 📁 api

Esta pasta contém uma pasta chamada endpoint que contém as rotas da
API e uma pasta chamada events, que contém os eventos que devem ser
registrados no startup e shutdown da aplicação.

#### 📁 core

Nesta pasta ficam os arquivos que dão sustentação a aplicação, neste
caso são as pastas:

1. controllers
2. database
3. dependencies
4. metadata
5. models
6. schemas
7. security

#### 📁 utils

Esta pasta é destinada a todo código que dá suporte a aplicação.

#### 📋 main.py

Este arquivo constitui o núcleo da aplicação FastAPI. Nele, encontramos
a definição da aplicação por meio da criação de uma instância da classe
FastAPI, que foi definida como:

    app: FastAPI

### 📁 configuration

Nesta pasta encontramos as configurações da nossa aplicação. As configurações
serão armazenadas como variáveis de ambiente, e podem ser definidas como
4 tipos/chaves:

    [default] -> Os valores contidos nessa chave, serão atribuido como padrão.
    [production] -> Os valores contidos nessa chave, serão atribuido em modo de produção.
    [development] -> Os valores contidos nessa chave, serão atribuido em modo de devesenvolvimento.
    [testing] -> Os valores contidos nessa chave, serão atribuido em modo de teste.

Os arquivos contidos nesta pasta são:

1. 📋 .secrets (deve ser criado por você)
2. 📋 configs.py
3. 📋 .settings.toml

#### 📋 .settings.toml

Neste arquivo ficarão os dados sensíveis que não deve subir para o repositório,
como, por exemplo:

    [default]
    JWT_SECRET = ""
    ALGORITHM = ""
    DATABASE_URL = ""
    
    [production]
    JWT_SECRET = ""
    DATABASE_URL = ""
    
    [development]
    JWT_SECRET = ""
    DATABASE_URL = ""
    
    [testing]
    JWT_SECRET = ""
    DATABASE_URL = ""

#### 📋 configs.py

Este arquivo possui a instância da classe Dynaconf que será usada
pela aplicação. Ela usa as variáveis de ambiente conforme
o modo que a aplicação está rodando. Este modo e definido através
da variável de ambiente FASTAPITEMPLATE_APP_RUNNING_MODE. A
instância da classe foi definida como:

    settings: Dynaconf

#### 📋 settings.toml

Neste arquivo ficarão as configurações menos sensíveis, mas não por isso,
menos essenciais, como, por exemplo:

    [default]
    API_URL = "/api/v1"
    SERVER_RELOAD = 1
    
    [production]
    API_URL = "/api/v1"
    
    [development]
    API_URL = "/api/v1"
    
    [testing]
    API_URL = "/api/v1"

### 📁 docker

Nesta pasta ficam os arquivos referente ao Docker, como exceção
do docker-compose.*.yaml

1. 📋 .dev.env
2. 📋 .prod.env
3. 📋 .test.env
4. 📋 Dockerfile.api

#### 📋 Arquivos *.env

Estes arquivos possuem as variáveis de ambiente que serão usadas
para criação dos containers através do docker-compose. Todos eles
possuem as mesmas chaves, mas os valores podem variar conforme
a necessidade. Abaixo um exemplo do arquivo:

    POSTGRES_DB=db_production
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=123
    FASTAPITEMPLATE_DATABASE_URL=postgresql+asyncpg://postgres:123@db:5432/db_production

As variáveis iniciadas com POSTGRES serão usadas para criação do banco,
já a variável FASTAPITEMPLATE_DATABASE_URL será usada para aplicação
para se conectar com banco de dados. Adapte de acordo com sua necessidade.

#### 📋 Dockerfile.api

Arquivo para definir a imagem da nossa aplicação.

### 📁 docs

Nesta pasta ficam os arquivos que retratam a documentação desta aplicação.
Como, por exemplo, README.md

### 📁 migrations

Essa pasta contém os arquivos referente as migrações do banco de dados. Estas
migrações foram criadas usando o alembic.

### 📁 tests

Ainda não foi implementado testes de exemplo

### 📋 .python-version

Arquivo refente a versão python usada neste projeto

### 📋 alembic.ini

Arquivo de configuração do alembic

### 📋 Arquivos docker-compose.*.yaml

Os arquivos docker-compose.yml são como guias de receitas para o Docker.
Ele diz ao Docker como configurar e interligar vários contêineres para
funcionarem juntos. Nesse arquivo, você especifica coisas como:
imagem de contêiner, serviço, portas, volumes, redes que eles vão usar
e até mesmo as variáveis de ambiente.

Para definir qual modo a aplicação irá rodar você deve definir a variável de ambiente
que fica dentro dos arquivos "docker-compose...". Tenha em mente que esta aplicação
é feita para rodar em containers até mesmo durante o desenvolvimento. Os arquivos
"docker-compose..." ficam na raiz do projeto.

Por exemplo:

    ...

    FASTAPITEMPLATE_APP_RUNNING_MODE=development

    ...

Existe um arquivo para cada modo que a aplicação poderá rodar, nesta aplicação
encontraremos:

1. docker-compose.dev.yaml
2. docker-compose.prod.yaml
3. docker-compose.test.yaml


### 📋 poetry.lock

Este arquivo registra as versões específicas de todas as
bibliotecas e dependências que seu projeto precisa para
funcionar corretamente.

### 📋 pyproject.toml

O arquivo pyproject.toml é um mapa de planejamento para projetos Python,
onde você define as configurações e metadados do projeto.
É um arquivo de configuração mais moderno e legível do que o antigo setup.py.
Nele, você especifica detalhes como o nome do projeto, a versão do
Python necessária, as dependências, scripts personalizados e até mesmo
configurações específicas do ambiente de desenvolvimento.

### 🔧 Clonando e Rodando

Siga os passos abaixo:

#### ▶️️ Clonando o Repositório:

```bash
git clone https://github.com/lspraciano/fastapiAPITemplate.git
```

#### ▶️️ Adapte o Conteúdo dos Arquivos Necessários:

No tópico sobre a estrutura do projeto vimos que alguns arquivos precisam
ser adaptados de acordo com sua necessidade. Os arquivos serão listados
abaixo para ajudar você:

1. 📋 docker/.dev.env
2. 📋 docker/.prod.env
3. 📋 docker/.test.env
4. 📋 configuration/.secrets.toml

Na dúvida reveja o tópico sobre a estrutura do projeto para entender
melhor qual o conteúdo desses arquivos.

#### ▶️️ Rodando

Após ajustar os arquivos básicos, vamos rodar a aplicação. Lembre que para cada
modo que a aplicação poderá ser iniciada temos um arquivo docker-compose...
para tal. Vamos neste exemplo rodar em modo de "development".

```bash
cd fastapiAPITemplate
docker compose -f docker-compose.dev.yaml up
```

Neste padrão de projeto, assim que você realizar alterações na aplicação, não
será necessário reiniciar o docker, pois "bindamos" a pasta para garantir o reload