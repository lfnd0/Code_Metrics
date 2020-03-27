# docs: https://radon.readthedocs.io/en/latest/api.html#module-radon.complexity

import os

from radon.cli.tools import iter_filenames
from radon.complexity import cc_visit
from radon.raw import analyze
from radon.metrics import h_visit

for filename in iter_filenames([r'./tests/test1.py']):

    with open(filename, encoding="utf8") as fobj:
        source = fobj.read()
    
    raw = analyze(source)
    hal = h_visit(source)
    blocks = cc_visit(source)
    
# Retorna todos os atributos do objeto '.__dir__()'
# Acessa um atributo do objeto 'nome_da_instância.nome_do_atributo'
print('Raw: ', raw)
print('Blocks: ', blocks)
print('Halstead: ', hal)