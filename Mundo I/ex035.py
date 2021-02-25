r1 = float(input('Digite um comprimento: '))
r2 = float(input('Digite um comprimento: '))
r3 = float(input('Digite um comprimento: '))

if r1 < r2 + r3 and  r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas acima podem formar um triângulo!')
else:
    print('As retas abaixo não podem formar um triângulo!')