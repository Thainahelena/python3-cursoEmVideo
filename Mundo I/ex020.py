from random import shuffle
aluno_1 = input('1º Aluno: ')
aluno_2 = input('2º Aluno: ')
aluno_3 = input('3º Aluno: ')
aluno_4 = input('4º Aluno: ')

lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
shuffle(lista_alunos)

print('A ordem de apresentação será:', lista_alunos)