from mysql.connector import connect
from contextlib import contextmanager

parametros = dict(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    database='code_metrics'
)

@contextmanager
def conectar():
    conexao = connect(**parametros)
    try:
        yield conexao
    finally:
        if(conexao and conexao.is_connected()):
            conexao.close()