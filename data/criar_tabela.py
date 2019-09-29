from conexao import conectar
from mysql.connector.errors import ProgrammingError

tabela_resultado_metricas = """
    CREATE TABLE IF NOT EXISTS resultado_metricas(
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(10) UNIQUE,
        loc_raw INT,
        lloc_raw INT,
        sloc_raw INT,
        hal_h1 INT,
        hal_h2 INT,
        hal_N1 INT,
        hal_N2 INT,
        hal_vocabulario INT,
        hal_tamanho INT,
        hal_volume DOUBLE,
        hal_dificuldade DOUBLE,
        hal_esforco DOUBLE,
        hal_tempo DOUBLE,
        hal_bugs DOUBLE,
        KEY(nome)
    )
"""

try:
    with conectar() as conexao:
        try:
            cursor = conexao.cursor()
            cursor.execute(tabela_resultado_metricas)
        except ProgrammingError as e:
            print(f'Erro: {e.msg}')
except ProgrammingError as e:
    print(f'Erro na conexão: {e.msg}')