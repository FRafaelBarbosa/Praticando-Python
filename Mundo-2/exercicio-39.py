from datetime import date

ano_atual = date.today().year
print('\033[1;32m-=-'*5,'Alistamento Militar','-=-'*5,'\033[m')
nascimento = int(input('Ano de nascimento: '))
print('\033[1;32m-=-'*6,'Verificando...','-=-'*5,'\033[m')
idade = ano_atual - nascimento

if idade < 18:
    print('\033[7;36mVocê possui {} anos e faltam {} anos para você fazer seu alistamento.\033[m'.format(idade, 18 - idade))
elif idade > 18:
    print('\033[7;31mVocê possui {} anos e passou {} anos do tempo de alistamento.\033[m'.format(idade, idade - 18))
else:
    print('\033[7;32mVocê possui {} anos e está na hora de fazer seu alistamento.\033[m'.format(idade))