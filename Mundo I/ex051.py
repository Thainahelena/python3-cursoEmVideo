soma = 0
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo_termo = primeiro_termo + (10 - 1) * razao

for numero in range(primeiro_termo, decimo_termo + razao, razao):
    print('{}'.format(numero), end=' → ')
print('ACABOU!!!')