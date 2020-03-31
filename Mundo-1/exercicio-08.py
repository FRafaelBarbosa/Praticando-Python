'''
Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
'''

nmetros = float(input('Entre com um valor: '))

metrosparacm = nmetros / 100
metrosparamm = nmetros /1000

print('{}m tem {}cm'.format(nmetros, metrosparacm), end = ' ')
print('{}m tem {}mm'.format(nmetros, metrosparamm))
