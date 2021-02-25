print('Bem-Vindo ao Conversor de Número!\nDigite um número inteiro para fazer a conversão.')
print('-=-' * 15)
numero = int(input('Digite o número para ser convertido: '))

print('   [ 1 ] para conversão em base binária\n   [ 2 ] para conversão em base octagonal\n   [ 3 ] para conversão em base hexadecimal')
base = int(input('Para qual base você deseja converter? '))

if base == 1:
      print('{} convertido em binário é igual a {}.'.format(numero, bin(numero)[2:]))
elif base == 2:
      print('{} convertido em octal é igual a {}.'.format(numero, oct(numero)[2:]))
elif base == 3:
      print('{} convertido em hexadecimal é igual a {}.'.format(numero, hex(numero)[2:]))
else:
      print('Opção Inválida. Tente Novamente!')