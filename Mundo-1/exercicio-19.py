from random import choice

primeiro = str(input('Primeiro Aluno: '))
segundo = str(input('Segundo Aluno: '))
terceiro = str(input('Terceiro Aluno: '))
quarto = str(input('Quarto Aluno: '))

lista = [primeiro, segundo, terceiro, quarto]

escolhido = choice(lista)

print('O aluno escolhido foi {}'.format(escolhido))
