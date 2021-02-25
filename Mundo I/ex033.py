a = int(input('Digite o valor 1: '))
b = int(input('Digite o valor 2: '))
c = int(input('Digite o valor 3: '))

# Verificar o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Verificar o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('-=-' * 10)
print('O número menor é o: {}'. format(menor))
print('O número maior é o: {}'.format(maior))