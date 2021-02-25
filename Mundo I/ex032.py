numero = int(input('Digite o ano para verificação: '))

if numero % 4 == 0 and numero % 100 != 0 or numero % 400 == 0:
    print('É um ano bissexto!')
else:
    print('Não é um ano bissexto!')