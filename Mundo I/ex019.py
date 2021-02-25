from random import choice
aluno_1 = input('Digite o nome do 1º aluno: ')
aluno_2 = input('Digite o nome do 2º aluno: ')
aluno_3 = input('Digite o nome do 3º aluno: ')
aluno_4 = input('Digite o nome do 4º aluno: ')

lista = [aluno_1, aluno_2, aluno_3, aluno_4]
escolhido = choice(lista)

print('O aluno(a) escolhido foi {}!'.format(escolhido))