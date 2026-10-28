# Gerenciador de Tarefas

Este projeto servirá aprimorarmos nossa lógica de programação ao mesmo tempo em que exploramos conceitos e técniicas de programação back-end e fullstack. Vamos utilizar e desenvolver o conceito de MVC (Model-View-Controller), algumass particularidades da Programação funcional, persistência de dados (MySQL), microframework Flask e gerenciador de pacotes do Python (Astral uv)

### Alguns passos iniciais para preparar o projeto:

1. Caso não esteja instalado, prepare o uv no seu OS. Você encontra o script de instalação no site <https://docs.astral.sh/uv/#installation>
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. Faça a inicialização do projeto com o comando:
```bash
uv init
```

Até então utilizávamos um layout de Pacote (Package Layout) denominado flat-layout. O uv adota uma estruturação mais moderna chamada *src-layout*, que previne erros de importação comuns chamadas `import `

3. Crie um ambiente virtual do Python
```bash
uv venv
```
Ative o ambiente virtual, se necessario:
```powershell
.\.venv\Script\Activate.ps1 # no Powershell do windows
source .venv/Scripts/Activate # no Git Bash do windows
source .venv/bin/Activate # no Bash do Linux
```

4. Instale o Flask
```bash
uv add flask
```
Será criado um arquivo uv.lock contendo as dependêcias (requerimentos) e versões dos pacotes dos pacostes do seu projeto.

5. Crie um arquivo `app.py` contendo o código inicial do projeto
```python
from flask import Flask

app = Flask(__name__)

@app.route('/test')
def test():
    return 'Servidor online!'
```

6. Teste a aplicação iniciando o servidor do Flask
```bash
uv run flask run
```