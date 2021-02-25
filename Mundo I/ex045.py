from time import sleep
import random

print('-=-' * 10)
print('   ======= JOKENPÔ =======')
print('-=-' * 10)
print('Suas opções são:'
      '\n  [ 1 ] PEDRA'
      '\n  [ 2 ] PAPEL'
      '\n  [ 3 ] TESOURA')
jogador = int(input('Digite sua escolha: '))
computador = random.choice([1, 2, 3])
PEDRA = 1
PAPEL = 2
TESOURA = 3

print('      JO')
sleep(1)
print('      KEN')
sleep(1)
print('      PÔ')

print('-=-' * 10)

if jogador == 1:
      print('Jogador jogou: PEDRA')
elif jogador == 2:
      print('Jogador jogou: PAPEL')
elif jogador == 3:
      print('Jogador jogou: TESOURA')
if computador == 1:
      print('Computador jogou: PEDRA')
elif computador == 2:
      print('Computador jogou: PAPEL')
elif computador == 3:
      print('Computador jogou: TESOURA')
print('-=-' * 10)

# PEDRA GANHA DA TESOURA
# PAPEL GANHA DA PEDRA
# TESOURA GANHA DO PAPEL

if (computador == 1 and jogador == 3) or (computador == 2 and jogador == 1) or (computador == 3 and jogador == 2):
      print('Computador GANHOU!')
elif (jogador == 1 and computador == 3) or (jogador == 2 and computador == 1) or (jogador == 3 and computador == 2):
      print('Jogador GANHOU!')
elif jogador == computador:
      print('Empate!')
else:
      print('Jogada INVÁLIDA!')
