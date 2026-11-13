
from src.tarefas.models.database import Database


class Tarefa:
    def __init__(self, id_tarefa=None, titulo_tarefa=None, data_conclusao=None):
        self.id_tarefa = id_tarefa
        self.titulo_tarefa = titulo_tarefa
        self.data_conclusao = data_conclusao

    @staticmethod
    def listarTarefa():
        """Retorna lista com todas as tarefas cadastradas."""
        sql = '''SELECT id_tarefa, titulo_tarefa, data_conclusao
        FROM tarefas LIMIT 100;'''

        with Database() as db:
            tarefas_banco = db.executar(sql)

        return tarefas_banco if tarefas_banco else []

    @staticmethod
    def inserir(titulo_tarefa, data_conclusao):
        """Insere uma nova tarefa no banco de dados."""
        sql = 'INSERT INTO tarefas (titulo_tarefa, data_conclusao) VALUES (%s, %s);'

        with Database() as db:
            db.executar(sql, (titulo_tarefa, data_conclusao))

    @staticmethod
    def carregarPorId(id_tarefa):
        """Busca uma única tarefa no banco pelo ID para edição."""
        sql = 'SELECT id_tarefa, titulo_tarefa, data_conclusao FROM tarefas WHERE id_tarefa = %s;'

        with Database() as db:
            resultado = db.executar(sql, (id_tarefa,))

        return resultado[0] if resultado else None

    @staticmethod
    def atualizar(id_tarefa, titulo_tarefa, data_conclusao):
        """Atualiza os dados de uma tarefa existente no banco."""
        sql = 'UPDATE tarefas SET titulo_tarefa = %s, data_conclusao = %s WHERE id_tarefa = %s;'

        with Database() as db:
            db.executar(sql, (titulo_tarefa, data_conclusao, id_tarefa))

    @staticmethod
    def apagar(id_tarefa):
        """Remove a tarefa do banco pelo ID."""
        sql = 'DELETE FROM tarefas WHERE id_tarefa = %s;'

        with Database() as db:
            db.executar(sql, (id_tarefa,))
