
soma = 0

print('\033[7;32mMultiplos de 3 ímpar: \033[m', end=' ')
for i in range(0, 500, 3):
    if(i % 2 == 1):
        soma += i
        print(i, end = ' ')


print('\033[7;31m\nSoma = {}\033[m'.format(soma))