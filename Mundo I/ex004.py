algo = input('Digite algo:')

print('O tipo primitivo desse valor é: ', type(algo))
print('Esse valor tem somente espaços?', algo.isspace())
print('Esse valor é um número?', algo.isnumeric())
print('Esse valor pode ser alfabético?', algo.isalpha())
print('Esse valor pode ser alfanumérico?', algo.isalnum())
print('Esse valor está em maiúsculo?', algo.isupper())
print('Esse valor está em minúsculo?', algo.islower())
print('Esse valor está capitalizado?', algo.istitle())