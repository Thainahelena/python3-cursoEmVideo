nome = input('Digite seu nome completo: ')

nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
nome_separado = nome.split()

nome_junto = ''.join(nome_separado)
nome_junto_tamanho = len(nome_junto)


print('   Seu nome maiúsculo é:', nome_maiusculo)
print('   Seu nome minúsculo é:', nome_minusculo)
print('   Seu nome tem:', nome_junto_tamanho, 'letras')
print('   Seu primeiro nome é {} e ele tem {} letras'.format(nome_separado[0],len(nome_separado[0])))


### Algoritmo alternativo:
"""nome = str(input('Digite seu nome completo: ')).strip()

print('Seu nome completo em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome completo em letras minusculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
# A quantidade de letras no nome é a quantidade de letras total menos quantos espaços o python contar!
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))"""

