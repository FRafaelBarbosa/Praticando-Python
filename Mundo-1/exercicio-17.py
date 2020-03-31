'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
triângulo retângulo, calcule e mostre o comprimento da hipotenusa
'''
import math

oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))

hipotenusa = ((oposto**2) + (adjacente**2))**(1/2)

print('A hipotenusa vai medir {:.2f}'.format(math.hypot(oposto, adjacente)))
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))