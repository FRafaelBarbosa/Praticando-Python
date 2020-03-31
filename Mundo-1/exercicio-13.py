'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
'''

salario = float(input('Qual o salário do funcionário? R$'))

novo = salario + ((15 / 100) * salario)

print('O salario do funcinário era de {:.2f} e com aumento de 15%, passa a receber {:.2f}'.format(salario, novo))