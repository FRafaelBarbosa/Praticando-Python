'''
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possiveis sobre ele.

'''

var = input('Digite algo: ')

print(type(var))
print(var.isalnum())
print(var.isalpha())
print(var.isdecimal())
print(var.isnumeric())
print(var.isspace())
print(var.islower())
print(var.isascii())