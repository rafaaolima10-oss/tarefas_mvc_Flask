
from flask import Flask, render_template, request, redirect, url_for
from src.tarefas.models.tarefa import Tarefa

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Pega os dados enviados pelo formulário de cadastro
        titulo = request.form.get('tituloTarefa')
        data = request.form.get('dataConclusao') or None

        # Insere a nova tarefa no banco de dados
        Tarefa.inserir(titulo, data)
        return redirect(url_for('index'))

    # Carrega todas as tarefas para exibir na página principal
    tarefas = Tarefa.listarTarefa()
    return render_template(
        'base.html',
        titulo="Lista de Tarefas",
        tarefas_da_pagina=tarefas,
        tarefa_a_editar=None
    )


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_tarefa(id):
    if request.method == 'POST':
        # Pega os novos valores enviados pelo formulário ao clicar em 'Atualizar'
        titulo = request.form.get('tituloTarefa')
        data = request.form.get('dataConclusao') or None

        # Salva as alterações no banco de dados
        Tarefa.atualizar(id, titulo, data)
        return redirect(url_for('index'))

    # Se for GET, busca a tarefa específica para preencher o formulário
    tarefa_selecionada = Tarefa.carregarPorId(id)

    # Carrega a lista completa para manter a tabela visível na tela
    tarefas = Tarefa.listarTarefa()

    return render_template(
        'base.html',
        titulo="Editar Tarefa",
        tarefas_da_pagina=tarefas,
        tarefa_a_editar=tarefa_selecionada
    )


@app.route('/apagar/<int:id>')
def apagar_tarefa(id):
    # Remove a tarefa do banco pelo ID
    Tarefa.apagar(id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
