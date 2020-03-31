from random import choice
from time import sleep
player = str(input('Pedra, Papel ou Tesoura? '))
lista = ['Pedra', 'Papel', 'Tesoura']
computador = choice(lista)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
if player == 'Pedra' and computador == 'Tesoura':
    print('Player: {} x Computador: {}'.format(player, computador))
    print('Você venceu!')
elif player == 'Papel' and computador == 'Pedra':
    print('Player: {} x Computador: {}'.format(player, computador))
    print('Você venceu!')
elif player == 'Tesoura' and computador == 'Papel':
    print('Player: {} x Computador: {}'.format(player, computador))
    print('Você venceu!')
elif player == computador:
    print('Player: {} x Computador: {}'.format(player, computador))
    print('Empate!')
else:
    print('Player: {} x Computador: {}'.format(player, computador))
    print('Você Perdeu!')