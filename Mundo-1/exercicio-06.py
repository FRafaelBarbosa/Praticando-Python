'''
Crie um algoritmo que leia um número e mostre seu dobro,
triplo, e raiz quadrada.
'''

n = float(input('Entre com um valor: '))

dobro = n * 2
triplo = n * 3
raizquadrada = n**(1/2)

print('O dobro de {:.2f} é {:.2f}'.format(n, dobro), end = ' ')
print('O triplo de {:.2f} é {:.2f}'.format(n, triplo), end = ' ')
print('A raiz quadrada de {:.2f} é {:.2f}'.format(n, raizquadrada))