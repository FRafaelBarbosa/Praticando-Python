print('{:=^40}'.format(' Taverna do Zé '))
produto = float(input('Preço do Produto: R$'))
print('''Escolha uma opção de pagamento: 
1 - A Vista dinheiro/cheque: 10% de desconto
2 - A Vista no cartão: 5% de desconto
3 - Em até 2x no cartão: sem juros
4 - 3x ou mais no cartão: 20% de juros''')
forma_de_pagamento = int(input('Qual a condição de Pagamento? '))
if forma_de_pagamento == 1:
    desconto = produto - (produto * (10/100))
    print('Sua compra de R${:.2f} ficará no valor de R${:.2f} COM DESCONTO.'.format(produto, desconto))
elif forma_de_pagamento == 2:
    desconto = produto - (produto * (5/100))
    print('Sua compra de R${:.2f} ficará no valor de R${:.2f} COM DESCONTO.'.format(produto, desconto))
elif forma_de_pagamento == 3:
    parcela = int(input('Quantas Parcelas? '))
    total = preco_do_produto / parcela
    print('Sua compra de R${:.2f} será parcelada em {}x de R${:.2f} SEM JUROS'.format(produto, parcela, total))
elif forma_de_pagamento == 4:
    parcela = int(input('Quantas Parcelas? '))
    preco_total = preco_do_produto + (preco_do_produto * (20/100))
    total = preco_total / parcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcela, total))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(produto, preco_total))
else:
    print('Escolha uma opção válida, tente novamente!')