r1 = float(input('Digite um comprimento: '))
r2 = float(input('Digite um comprimento: '))
r3 = float(input('Digite um comprimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas acima podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ESÓSCELES!')
else:
    print('Você não pode formar um triângulo!')