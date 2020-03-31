num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
'''
num = input('Digite um numero de 0 a 9999: ')

num.split()

print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))



num = int(input('Digite um número de 0 a 9999: '))
valor = str(num)
print('Unidade: {}'.format(valor[3]))
print('Dezena: {}'.format(valor[2]))
print('Centena: {}'.format(valor[1]))
print('Milhar: {}'.format(valor[0]))

'''