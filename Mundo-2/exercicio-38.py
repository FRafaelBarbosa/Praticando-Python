num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

if num1 > num2:
    print('O \033[1;31mprimeiro número\033[m é maior.')
elif num2 > num1:
    print('O \033[1;31msegundo número\033[m é maior.')
else:
    print('\033[1;31mNão existe\033[m valor maior, os dois são iguais.')