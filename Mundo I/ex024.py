cidade = str(input('Digite a cidade que você nasceu: ').upper())
boleano = 'SANTO' in cidade.split()[0]

print('Tem a palavra "SANTO" em {}? {}'.format(cidade, boleano))

### Algoritmo alternativo:
"""cidade = str(input('Escreva sua cidade: ')).strip()
print(cidade[0:5].upper() == 'SANTO')"""