soma = 0
contador = 0
for numero in range(0, 6):
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        soma += numero
        contador += 1
print('A soma dos {} números pares digitados é: {}'.format(contador, soma))