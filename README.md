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
  ou:

    radon cc nome_do_arquivo.py -s
  ou:
  
    radon cc nome_do_arquivo.py -a -nc
  ### Índice de manutenção:
    radon mi nome_do_arquivo.py
  ### Métricas de Halsted:
    radon hal nome_do_arquivo.py