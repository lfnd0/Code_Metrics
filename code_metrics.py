import os

from radon.cli.tools import iter_filenames
from radon.complexity import cc_visit
from radon.raw import analyze
from radon.metrics import h_visit

from data.conexao import conectar
from mysql.connector.errors import ProgrammingError, IntegrityError

for filename in iter_filenames([r'./tests']):

    with open(filename, encoding="utf8") as fobj:
        source = fobj.read()
    
    # blocks = cc_visit(source)
    # print(f'Complexidade ciclomática: {blocks[0].complexity}')
    raw = analyze(source)
    hal = h_visit(source)

    sql = 'INSERT INTO resultado_metricas (nome, loc_raw, lloc_raw, sloc_raw, hal_h1, hal_h2, hal_N1, hal_N2, hal_vocabulario, hal_tamanho, hal_volume, hal_dificuldade, hal_esforco, hal_tempo, hal_bugs) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    args = (os.path.basename(filename), raw.loc, raw.lloc, raw.sloc, hal.total.h1, hal.total.h2, hal.total.N1, hal.total.N2, hal.total.vocabulary, hal.total.length, hal.total.volume, hal.total.difficulty, hal.total.effort, hal.total.time, hal.total.bugs)
    
    try:
        with conectar() as conexao:
            try:
                cursor = conexao.cursor()
                cursor.execute(sql, args)
                conexao.commit()
            except ProgrammingError as e:
                print(f'Erro: {e.msg}')
            else:
                print(f'Nome do arquivo: {os.path.basename(filename)}')
                # print(f'Complexidade ciclomática: {blocks[0].complexity}')
                print(f'Métricas brutas: LOC={raw.loc}, LLOC={raw.lloc}, SLOC={raw.sloc}')
                print(f'Métricas de Halstead: h1={hal.total.h1}, h2={hal.total.h2}, N1={hal.total.N1}, N2={hal.total.N2}, Vocabulário={hal.total.vocabulary}, Tamanho={hal.total.length}, Volume={hal.total.volume}, Dificuldade={hal.total.difficulty}, Esforço={hal.total.effort}, Tempo={hal.total.time}, Bugs={hal.total.bugs}\n')
    except IntegrityError as e:
        print(f'Erro: {e.msg}')