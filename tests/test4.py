info = """
Observe e memorize as posições para suas jogadas. Digite apenas os números usados no exemplo:
     |   |       0 | 1 | 2          -9| -8|-7
  ---+---+---   ---+---+---        ---+---+---
     |   |       3 | 4 | 5    ou    -6| -5|-4
  ---+---+---   ---+---+---        ---+---+---  
     |   |       6 | 7 | 8          -3| -2|-1
"""

print(info)
 
matriz = ['','','',
          '','','',
          '','','']
 
print ("Jogador Nº 1 = X e Jogador Nº 2 = O")

repetir = 0
velha = 0
 
jogador1 = input("Digite o nome do Jogador Nº 1: ")
jogador2 = input("Digite o nome do Jogador Nº 2: ")

print("""Antenção {} e {}, nessa versão do Jogo da Velha, o jogador que digitar algum caractere diferente dos mostrados
no exemplo ou uma posição preenchida, perderá a partida automaticamente dando a vitória para seu adversário.""".format(jogador1, jogador2))

for i in range(9):
        if repetir%2 == 0:
            try:
                try:
                    linha = int(input("{}, faça sua jogada: ".format(jogador1)))
                    if matriz[linha] == '':
                        matriz[linha] = 'X'
                    else:
                        print("Nós te avisamos, você perdeu! Porque jogou uma posição preenchida. :p")
                        break
                except ValueError:
                    print("Nós te avisamos, você perdeu! Porque digitou um caractere diferente dos mostrados no exemplo. :p")
                    break
            except IndexError:
                print("Nós te avisamos, você perdeu! Porque digitou um número diferente dos mostrados no exemplo. :p")
                break
            print('\t %s | %s | %s' % (matriz[0], matriz[1], matriz[2]))
            print('\t---------')
            print('\t %s | %s | %s' % (matriz[3], matriz[4], matriz[5]))
            print('\t---------')
            print('\t %s | %s | %s' % (matriz[6], matriz[7], matriz[8]))
 
        else:
            try:
                try:
                    linha = int(input("{}, faça sua jogada: ".format(jogador2)))
                    if matriz[linha] == '':
                        matriz[linha] = 'O'
                    else:
                        print("Nós te avisamos, você perdeu! Porque jogou uma posição preenchida. :p")
                        break
                except ValueError:
                    print("Nós te avisamos, você perdeu! Porque digitou um caractere diferente dos mostrados no exemplo. :p")
                    break
            except IndexError:
                print("Nós te avisamos, você perdeu! Porque digitou um número diferente dos mostrados no exemplo. :p")
                break
            print('\t %s | %s | %s' % (matriz[0], matriz[1], matriz[2]))
            print('\t---------')
            print('\t %s | %s | %s' % (matriz[3], matriz[4], matriz[5]))
            print('\t---------')
            print('\t %s | %s | %s' % (matriz[6], matriz[7], matriz[8]))

        repetir += 1

        if((matriz[0] == matriz[1] == matriz[2] == 'X') or
            (matriz[3] == matriz[4] == matriz[5] == 'X') or
            (matriz[6] == matriz[7] == matriz[8] == 'X')):
            print("{} venceu! Parabéns! :D".format(jogador1))
            break
        else:
             velha += 1
                 
        if((matriz[0] == matriz[1] == matriz[2] == 'O') or
            (matriz[3] == matriz[4] == matriz[5] == 'O') or
            (matriz[6] == matriz[7] == matriz[8] == 'O')):
            print("{} venceu! Parabéns! :D".format(jogador2))
            break
        else:
            velha += 1

        if((matriz[0] == matriz[3] == matriz[6] == 'X') or
            (matriz[1] == matriz[4] == matriz[7] == 'X') or
            (matriz[2] == matriz[5] == matriz[8] == 'X')):
            print("{} venceu! Parabéns! :D".format(jogador1))
            break
        else:
             velha += 1
                 
        if((matriz[0] == matriz[3] == matriz[6] == 'O') or
            (matriz[1] == matriz[4] == matriz[7] == 'O') or
            (matriz[2] == matriz[5] == matriz[8] == 'O')):
            print("{} venceu! Parabéns! :D".format(jogador2))
            break
        else:
            velha += 1

        if((matriz[2] == matriz[4] == matriz[6] == 'X') or
            (matriz[0] == matriz[4] == matriz[8] == 'X')):
            print("{} venceu! Parabéns! :D".format(jogador1))
            break
        else:
             velha += 1
               
        if((matriz[2] == matriz[4] == matriz[6] == 'O') or
            (matriz[0] == matriz[4] == matriz[8] == 'O')):
            print("{} venceu! Parabéns! :D".format(jogador2))
            break
        else:
            velha += 1
        
        if velha == 54:
            print("DEU VELHA! Ahhh... Essa partida foi acirradíssima! :D")