'''
Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

'''

n = int(input('Entre com um valor: '))

antecessor = n - 1
sucessor = n + 1

msg = 'o antecessor do número {} é {} e seu sucessor é {}'.format(n, antecessor, sucessor)
print(msg)