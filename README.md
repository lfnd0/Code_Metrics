# Radon Code Metrics


  ## Informações:
   * Documentação: [Radon 2.4.0](https://radon.readthedocs.io/en/latest/index.html)
   * Repositório: [GitHub](https://github.com/rubik/radon)
   * PyPI: [Project Radon](https://pypi.org/project/radon/)


  ## Instalação do ambiente virtual:
    python -m venv env


  ## Instalação do Radon:  
    pip install radon


  ## Comandos:
  ### Ajuda:
    radon --help
  ### LOC, LLOC e SLOC: 
    radon raw nome_do_arquivo.py
  ### Complexidade ciclomática:
    radon cc nome_do_arquivo.py
   #### Listagem com sumário:

    radon cc nome_do_arquivo.py -s
   #### Cálculo da média final:
  
    radon cc nome_do_arquivo.py -a
   #### Cáculo da média total:
  
    radon cc nome_do_arquivo.py --total-average
   #### Impressão dos resultados de um determinado grau (A a F):

    radon cc nome_do_arquivo.py -a -na
   #### Impressão dos resultados de um determinado grau (D a F):

    radon cc nome_do_arquivo.py -a -nd
   #### Impressão dos resultados de um determinado grau (C):

    radon cc nome_do_arquivo.py -a -nc
  ### Índice de manutenção:
    radon mi nome_do_arquivo.py
  ### Métricas de Halsted:
    radon hal nome_do_arquivo.py