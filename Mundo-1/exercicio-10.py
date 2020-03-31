'''
crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
quantos dolares ela pode comprar. Considere US$1.00 = R$3.27
'''

dinheiro = float(input('Digite quanto dinheiro você tem em R$: '))

dolar = dinheiro / 3.27

print('Com R${} você pode comprar US${:.2f}'.format(dinheiro, dolar))