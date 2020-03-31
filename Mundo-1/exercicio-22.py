
nome = str(input('Nome completo: ')).strip()

print('Seu nome em maiúsculo é: {}'.format(nome.upper()))
print('Seu nome em minúsculo é: {}'.format(nome.lower()))
print('Seu nome tem ao todo: {}'.format(len(nome.replace(' ', ''))))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))