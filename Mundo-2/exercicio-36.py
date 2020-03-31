valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

quantParcelas = anos * 12
prestacaoMensal = valor / quantParcelas

if prestacaoMensal > salario * 0.3:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor, anos, prestacaoMensal))
    print('\033[7;31mEmprestimo Negado!\033[m')
else:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor, anos, prestacaoMensal))
    print('\033[7;32mEmprestimo pode ser CONCEDIDO!\033[m')

