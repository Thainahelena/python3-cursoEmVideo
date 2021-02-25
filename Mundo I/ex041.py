from datetime import date
print('Bem-Vindo a Confederação Nacional de Natação!\nAgradecemos seu interesse.\nDescubra sua categoria de natação aqui!')

print('-=-' * 10)
ano_nascimento = int(input('Digite o ano de seu nascimento para verificação: '))
print('-=-' * 10)

ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade <= 9:
    print('O atleta tem {} anos e participará da categoria:  \033[31mMIRIM\033[m'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos e participará da caterogia:  \33[32mINFATIL\033[m'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos e participará da categoria:  \033[33mJUNIOR\033[m'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos e participará da categoria:  \033[35mSENIOR\033[m'.format(idade))
else:
    print('O atleta tem {} anos e participará da categoria:  \033[36mMASTER\033[m'.format(idade))