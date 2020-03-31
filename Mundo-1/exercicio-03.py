'''
Crie um programa que leia dois numeros e mostre a soma entre eles.

'''

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
soma = num1 + num2
msg = 'A soma entre {valor1} e {valor2} vale {total}.'.format(valor1 = num1, 
                                                                valor2 = num2, 
                                                                total = soma)
print(msg)
