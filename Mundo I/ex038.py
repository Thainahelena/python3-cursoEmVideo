print('Este programa descobrirá qual valor digitado é maior e qual valor digitado é menor. Experimente!')
print('-=-' * 10)
v1 = float(input('Digite o 1º valor: '))
v2 = float(input('Digite o 2º valor: '))
print('-=-' * 10)
if v1 > v2:
    print('   O primeiro valor que você digitou foi {} e ele é o maior!'.format(v1))
elif v2 > v1:
    print('   O segundo valor que você digitou foi {} e ele é o maior!'.format(v2))
else:
    print('   Não existe valor maior ou valor menor. O valor {} é exatamente igual ao valor {}.'.format(v1, v2))
