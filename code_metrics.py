from radon.raw import analyze
from radon.metrics import mi_visit
from radon.complexity import cc_visit
from radon.cli.tools import iter_filenames
from radon.metrics import h_visit

# Iter through filenames starting from the current directory,
# you can pass ignore or exclude patterns here (as strings)
# for example: ignore='tests,docs'.
for filename in iter_filenames([r'C:\Users\luizfernando\Documents\Projetos\Radon_Metricas_Codigo\tests\test1.py']):
    with open(filename, encoding="utf8") as fobj:
        source = fobj.read()

    # get CC blocks
    # blocks = cc_visit(source)
    
    # get MI score
    # mi = mi_visit(source, True)
    
    # get RAW metrics
    raw = analyze(source)
    
    # get HAL metrics
    hal = h_visit(source)
    
    # Now do what you want with the data
    # print(blocks)
    # print(mi)
    print(raw)
    print(hal)