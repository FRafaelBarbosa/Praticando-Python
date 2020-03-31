from random import randint

computador = randint(0, 5)
print('Adivinha o número que o computador "Pensou".')
usuario = int(input('Digite um número: '))
if usuario == computador:
    print('Usuário: {} e Computador: {}'.format(usuario, computador))
    print('PARABÉNS! Você venceu!')
else:
    print('Usuário: {} e Computador: {}'.format(usuario, computador))
    print('Você perdeu!')