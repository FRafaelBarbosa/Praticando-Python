from datetime import date

print('\033[1;32m-=-'*5,'Confederação Nacional de Natação','-=-'*5,'\033[m')
ano = int(input('Ano de nascimento: '))
print('\033[1;32m-=-'*8,'Verificando...','-=-'*5,'\033[m')
idade = date.today().year - ano
print('\033[1;32m-=-'*5,'Sua Categoria...','-=-'*5,'\033[m')
if idade < 10:
    print('Você tem {} anos e faz parte da categoria \033[7;31mMIRIM\033[m.'.format(idade))
elif idade < 15:
    print('Você tem {} anos e faz parte da categoria \033[7;32mINFANTIL\033[m.'.format(idade))
elif idade < 20:
    print('Você tem {} anos e faz parte da categoria \033[7;33mJUNIOR\033[m.'.format(idade))
elif idade < 21:
    print('Você tem {} anos e faz parte da categoria \033[7;34mSÊNIOR\033[m.'.format(idade))
else:
    print('Você tem {} anos e faz parte da categoria \033[7;35mMASTER\033[m.'.format(idade))