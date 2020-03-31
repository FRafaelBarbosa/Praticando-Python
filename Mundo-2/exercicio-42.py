print('\033[1;32m-=-'*5,'Verificar Retângulo','-=-'*5,'\033[m')
r1 = float(input('Digite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))
print('\033[1;32m-=-'*6,'Verificando...','-=-'*5,'\033[m')

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um TRIÂNGULO', end = ' ')
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('EQUILATERO!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('ISÓSCELES!')
    else:
        print('ESCALENO!')
else:
    print('Não pode formar um TRIÂNGULO!')
