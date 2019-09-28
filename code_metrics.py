import os
from radon.cli.tools import iter_filenames
# from radon.complexity import cc_visit
from radon.raw import analyze
from radon.metrics import h_visit

for filename in iter_filenames([r'C:\Users\luizfernando\Documents\Projetos\Code_Metrics\tests\test1.py']):

    with open(filename, encoding="utf8") as fobj:
        source = fobj.read()

    # blocks = cc_visit(source)
    raw = analyze(source)
    hal = h_visit(source)

    print(f'Nome do arquivo: {os.path.basename(filename)}')
    # print(f'Complexidade ciclomática: {blocks[0].complexity}')
    print(f'Métricas brutas: LOC={raw.loc}, LLOC={raw.lloc}, SLOC={raw.sloc}')
    print(f'Halstead: h1={hal.total.h1}, h2={hal.total.h1}, N1={hal.total.N1}, N2={hal.total.N2}, Vocabulário={hal.total.vocabulary}, Tamanho={hal.total.length}, Volume={hal.total.volume}, Dificuldade={hal.total.difficulty}, Esforço={hal.total.effort}, Tempo={hal.total.time}, Bugs={hal.total.bugs}\n')
