input('Pressione ENTER para começar')

soma = 0
contador = 0
for numero in range(1, 500, 2):
  if numero % 3 == 0:
    soma += numero
    contador += 1
print('A soma de todos os {} valores solicitados é {}'. format(contador, soma))