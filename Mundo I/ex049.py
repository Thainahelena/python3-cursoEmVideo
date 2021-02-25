numero = int(input('Digite um número para visualizar sua tabuada: '))

for base in range(0, 11):
    print('{} x {:2} ='.format(numero, base), numero * base)