'''
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.
'''

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))

media = (nota1 + nota2) / 2

print('A media do aluno é {:.2f}'.format(media))