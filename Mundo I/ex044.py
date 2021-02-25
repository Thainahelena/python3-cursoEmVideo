print('===== Bem-Vindo a Loja Virtual!!! =====')
print('-=-' * 20)
produto = float(input('Digite o preço das compras: '))
print('-=-' * 20)
print('FORMAS DE PAGAMENTO\n   [ 1 ] para a vista no dinheiro ou cheque\n   [ 2 ] para a vista no cartão\n   [ 3 ] para até 2x no cartão\n   [ 4 ] para 3x ou mais no cartão')
pagamento = int(input('Digite a forma de pagamento: '))

if pagamento == 1:
    print('Você ganhou 10% de desconto!\nPagará R${:.2f} pelo produto.'.format(produto * 0.9))
elif pagamento == 2:
    print('Você ganhou 5% de desconto!\nPagará R${:.2f} pelo produto.'.format(produto * 0.95))
elif pagamento == 3:
    parcela = produto / 2
    print('Sua compra será parcelada em {}x de R$ {:.2f} sem juros.\nPagará R${:.2f} pelo produto.'.format(2, parcela, produto))
elif pagamento == 4:
    parcela = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R${:.2f} com juros.\nSua compra de {:.2f} terá como preço final R${:.2f}.'.format(parcela, (produto * 1.20)/parcela, produto, produto * 1.20))
else:
    print('Forma de pagamento desconhecida. As formas de pagamento variam entre o número 1 e 4.')

print('-=-' * 20)