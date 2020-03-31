print('\033[1;32m-=-'*5,'Verificar IMC','-=-'*5,'\033[m')
peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é a sua altura? '))
print('\033[1;32m-=-'*6,'Verificando...','-=-'*5,'\033[m')

imc = peso / (altura * altura)

if imc < 18.5:
    print('\033[7;31mVocê se encontra Abaixo do Peso.\033[m')
elif imc < 25:
    print('\033[7;32mVocê se encontra com Peso Ideal.\033[m')
elif imc < 30:
    print('\033[7;33mVocê se encontra com Sobrepeso.\033[m')
elif imc < 40:
    print('\033[7;34mVocê se encontra com Obesidade.\033[m')
else:
    print('\033[7;35mVocê se encontra com Obesidade Mórbida.\033[m')