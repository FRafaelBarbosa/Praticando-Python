'''
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua áre e a
quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m²
'''


largura = float(input('Largura da parede em metros: '))
altura = float(input('Altura da parede em metros: '))

area_da_parede = largura * altura

litro_de_tinta = area_da_parede / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {}.'.format(largura, altura, area_da_parede))
print('Para pintar essa parede, você precisará de {}l de tinta'.format(litro_de_tinta))
