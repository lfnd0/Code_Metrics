# Radon Code Metrics


  ## Informações:
   * Documentação: [Radon 2.4.0](https://radon.readthedocs.io/en/latest/index.html)
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
    radon cc nome_do_arquivo.py -s
  ### Índice de manutenção:
    radon mi nome_do_arquivo.py
  ### Métricas de Halsted:
    radon hal nome_do_arquivo.py