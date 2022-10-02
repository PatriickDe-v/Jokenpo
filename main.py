from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''' Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

usuario = int(input('Qual é a sua jogada? '))
print('-=' * 15)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[usuario]}')
print('-=' * 15)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')

if computador == 0:  # computador jogou PEDRA
    if usuario == 0:
        print('EMPATE')
    elif usuario == 1:
        print('JOGADOR VENCE')
    elif usuario == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVALIDA!')

elif computador == 1:  # computador jogou PAPEL
    if usuario == 0:
        print('COMPUTADOR VENCE')
    elif usuario == 1:
        print('EMPATE')
    elif usuario == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVALIDA!')

elif computador == 2:  # computador jogou TESOURA
    if usuario == 0:
        print('JOGADOR VENCEU')
    elif usuario == 1:
        print('COMPUTADOR VENCEU')
    elif usuario == 2:
        print('EMPATE')
    else:
        print('JOGADA INVALIDA!')
