from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
Jogador = int(input('Qual é a sua jogada?'))
print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA!!!')
print('-=' * 11)
print('Computador Escolheu{}'.format(itens[computador]))
print('Jogador Escolheu {}'.format(itens[Jogador]))
print('-=' * 11)
if computador == 0: # COMPUTADOR JOGOU PEDRA
    if Jogador == 0:
        print('EMPATE')
    elif Jogador == 1:
        print('JOGADOR VENCE')
    elif Jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVALIDA!')

elif computador == 1: # COMPUTADOR JOGOU PAPEL
    if Jogador == 0:
        print('COMPUTADOR VENCE')
    elif Jogador == 1:
        print('EMPATE')
    elif Jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA!')

elif computador == 2: # COMPUTADOR JOGOU TESOURA
    if Jogador == 0:
        print('JOGADOR VENCE')
    elif Jogador == 1:
        print('COMPUTADOR VENCE')
    elif Jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA!')
