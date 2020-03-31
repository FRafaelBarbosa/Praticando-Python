print('\033[1;32m-=-'*5,'Média das Notas','-=-'*5,'\033[m')
n1 = float(input('Nota 01: '))
n2 = float(input('Nota 02: '))
print('\033[1;32m-=-'*6,'Verificando...','-=-'*5,'\033[m')

media = (n1 + n2) / 2

if media < 5.0:
    print('\033[7;31mSua média foi de {:.1f} e está abaixo de 5.0, você está REPROVADO!\033[m'.format(media))
elif media < 7.0:
    print('\033[7;33mSua média foi de {:.1f}, você se encontra de RECUPERAÇÃO!\033[m'.format(media))
else:
    print('\033[7;32mSua média foi de {:.1f}, você está APROVADO!\033[m'.format(media))