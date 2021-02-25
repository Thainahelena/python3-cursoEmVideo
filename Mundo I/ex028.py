print('O computador está pensando em um número de 0 a 5!')

import random
from time import sleep
numero = (0, 1, 2, 3, 4, 5)
num = random.choice(numero)
print('Pensando...')
sleep(2)

usuario = int(input(('Em qual número o computador pensou? ')))
print('PROCESSANDO...')
sleep(2)

if usuario == num:
    print('Que chute perfeito! O computador havia pensado no número: {}!'.format(num))
elif usuario > 5:
    print('O computador pensou em número de 0 a 5, não em um número maior que 5!')
else:
    print('Chute errado! O computador pensou no número {}!'.format(num))


### Algoritmo alternativo:
"""from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 18)
print('Vou pensar em número entre 0 e 5. Tente adivinhar... ')
print('-=-' * 18)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no número {}!'.format(computador, jogador))"""