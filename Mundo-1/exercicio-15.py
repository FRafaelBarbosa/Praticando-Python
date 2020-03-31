'''
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado
e a quantidade de dias pelos os quais ele foi alugado. Calcule o preço a pagar, sabendo que
o carro custa R$60 por dia e R$0.15 por km rodado.
'''

dias = float(input('Quantos dias de aluguel? '))
km = float(input('Quantos KM foram percorridos? '))

valor_total = (km * 0.15) + (dias * 60.00)

print('O total a pagar é de {:.2f}'.format(valor_total))