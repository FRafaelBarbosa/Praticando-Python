nome = str(input('Nome completo: ')).strip()

lista = nome.split()

print('Primeiro nome: {}'.format(lista[0]))
print('Ultimo nome: {}'.format(lista[len(lista) - 1]))


'''
nome = str(input('Nome completo: ')).strip()

lista = nome.split()

print('Primeiro nome: {}'.format(lista[0]))
lista.reverse()
print('Ultimo nome: {}'.format(lista[0]))

'''