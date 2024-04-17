<a href="https://wakatime.com/badge/user/739793a6-a4fb-4d88-b1e6-f79a9182d930/project/018e5da1-a102-4172-9bd4-4d61e140e96c"><img src="https://wakatime.com/badge/user/739793a6-a4fb-4d88-b1e6-f79a9182d930/project/018e5da1-a102-4172-9bd4-4d61e140e96c.svg" alt="wakatime"></a>



# api_conversao_monetaria
API em Python+Django, que responde um JSON, para conversão monetária. Usa uma moeda de lastro (USD) e faz conversões entre diferentes moedas com cotações de verdade e atuais


# Procedimentos de preparação e execução

## preparando o terreno


### clonando o REPO
para clonar o REPO, execute o comando abaixo
```bash
git clone https://github.com/eniodefarias/api_conversao_monetaria.git
cd api_conversao_monetaria
```
para executar o projeto siga para esta instrução: [executando-o-projeto](#executando-o-projeto)


### copiando o REPO
```bash
mkdir api_conversao_monetaria
git init
git remote add origin  https://github.com/eniodefarias/api_conversao_monetaria.git 
git pull -f origin main
git checkout main
```

### executando o projeto
instrucoes


# Desenvolvendo o projeto

## Briefing, descrição e requisitos
### Desafio Técnico desenvolvedor backend Python/Django
Construa uma API, que responda JSON, para conversão monetária. Ela deve ter uma moeda de lastro (USD) e fazer conversões entre diferentes moedas com cotações de verdade e atuais.
 - A API deve, originalmente, converter entre as seguintes moedas:
   - USD
   - BRL
   - EUR
   - BTC
   - ETH
 - Ex: USD para BRL, USD para BTC, ETH para BRL, etc...
 - A requisição deve receber como parâmetros: A moeda de origem, o valor a ser convertido e a moeda final.
   - Ex: ?from=BTC&to=EUR&amount=123.45

### Requisitos
 - O código precisa rodar em Linux Ubuntu (preferencialmente como container Docker)
 - Para executar seu código, deve ser preciso apenas rodar os seguintes comandos:
```text
git clone seu-fork
cd seu-fork
comando para instalar dependências
comando para executar a aplicação 
 ```
 - A API pode ser escrita com ou sem a ajuda de frameworks (À sua escolha)

### Critérios de avaliação
 - Organização do código: Separação de módulos, view e model, back-end e front-end
 - Clareza: O README explica de forma resumida qual é o problema e como pode rodar
a aplicação?
 - Assertividade: A aplicação está fazendo o que é esperado? Se tem algo faltando, o README explica o porquê?
 - Legibilidade do código (incluindo comentários)
 - Segurança: Existe alguma vulnerabilidade clara?
 - Cobertura de testes (Não esperamos cobertura completa)
 - Histórico de commits (estrutura e qualidade)
 - Escolhas técnicas: A escolha das bibliotecas, banco de dados, arquitetura, etc, é a melhor escolha para a aplicação?

---

 ## Criando o ambiente Django

 - criando o venv no diretorio do projeto, utilizarei comandos para o Linux:
   -  ```bash
        mkdir api_conversao_monetaria
        cd api_conversao_monetaria
        $HOME/.pyenv/shims/python3 -m venv .venv
        ```

 - ativando o VENV, instalando depedencias:
   -  ```bash
        source .venv/bin/activate
        pip install django
        python -m pip install --upgrade pip
        cat requeriments.txt|sort|uniq| grep -v '#' | xargs -n 1 pip3 install
        ```

 -  ~~instalando e criando o django diretamente sem ativar o VENV (não use este metodo)~~
  - ~~.venv/Scripts/python.exe -m pip install django~~
  - ~~.venv/Scripts/python.exe -m django-admin startproject api_cambio~~


 - Criando o projeto django:
   - ```bash
      django-admin startproject api_cambio 
        ```

 - Criando as pastas e arquivos para começar o projeto django:
   - ```bash          
     mkdir -p api_cambio/app1/migrations/ api_cambio/app2/migrations/; 
     touch api_cambio/app1/migrations/__init__.py api_cambio/app2/migrations/__init__.py
     touch api_cambio/app1/__init__.py  api_cambio/app2/__init__.py
     touch api_cambio/app1/admin.py api_cambio/app2/admin.py
     touch api_cambio/app1/apps.py api_cambio/app2/apps.py
     touch api_cambio/app1/models.py api_cambio/app2/models.py 
     touch api_cambio/app1/tests.py api_cambio/app2/tests.py
     touch api_cambio/app1/views.py api_cambio/app2/views.py
        ```

 - com os arquivos criados e quentinhos, vamos criar a APP1 que utilizará a lib **forex_python**
   - criar a view no api_cambio/app1/views.py 
   - e tambem adicionar a rota no api_cambio/urls.py


---


assasa
