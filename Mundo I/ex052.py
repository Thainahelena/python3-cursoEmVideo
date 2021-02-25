numero = int(input("Digite um numero inteiro: "))

total = 0
for posicao in range(1, numero + 1):
    if numero % posicao == 0:
        total += 1
if total == 2:
    print('numero é primo')
else:
    print('numero não é primo')