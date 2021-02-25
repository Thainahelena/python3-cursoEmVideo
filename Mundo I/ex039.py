from datetime import date
print('Bem-Vindo ao programa de alistamento militar! Digite sua idade para saber se deve se alistar.')

print('-=-' * 10)
ano_nascimento = int(input('Digite o ano de seu nascimento: '))
print('-=-' * 10)

ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade < 18:
    print('> \033[31m{} anos\033[m ? Você ainda não tem idade suficiente para se alistar ao serviço militar.\n Faltam {} anos para que você possa fazer isso!\n Seu alistamento será em {}.'.format(idade, (18-idade), (ano_atual + (18-idade))))
elif idade == 18:
    print('> \033[36m{} anos\033[m ? Esta na hora de você se alistar!'.format(idade))
else:
    print('> \033[31m{} anos\033[m ? Já passou o seu tempo de alistamento.\n Fazem {} anos que você deveria ter se alistado!\n Seu alistamento deveria ter sido em {}.'.format(idade, (idade-18), ano_atual - (idade-18)))