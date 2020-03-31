numero = int(input('Digite um número inteiro: '))

print('''Escolha uma das bases para conversão
\033[1;31m1 - Binário\033[m
\033[1;32m2 - Octal\033[m
\033[1;33m3 - Hexadecimal\033[m''')
opcao = int(input('Digitar opção: '))

if opcao == 1:
    print('{} convertido para \033[1;31mBinário\033[m é igual a {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para \033[1;32mOctal\033[m é igual a {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para \033[1;33mHexadecimal\033[m é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção invalida, tente novamente.')