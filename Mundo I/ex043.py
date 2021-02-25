print('Bem-Vindo a Calculadora do Índice de Massa Corporal!\nInsira as informações abaixo para verificar o status de sua saúde.')

print('-=-' * 10)
altura = float(input('  Digite sua altura: '))
peso = float(input('  Digite seu peso: '))
print('-=-' * 10)
imc = peso / (altura*altura)

if imc < 18.5:
    print('  Seu IMC é \033[31m{:.2f}\033[m\n  É menor do que 18,5.\n  Por isso você está \033[31mabaixo do peso\033[m!'.format(imc))
elif 18.5 <= imc < 25:
    print('  Seu IMC é \033[36m{:.2f}\033[m\n  Esta entre 18,5 e 25.\n  Por isso você está em seu \033[36mpeso ideal\033[m!'.format(imc))
elif 25 <= imc < 30:
    print('  Seu IMC é \033[34m{:.2f}\033[m\n  Esta entre 25 e 30.\n  Por isso você está no \033[34msobrepeso\033[m!'.format(imc))
elif 30 <= imc < 40:
    print('  Seu IMC é \033[31m{:.2f}\033[m\n  Esta entre 30 e 40.\n  Por isso você tem \033[31mobesidade\033[m!'.format(imc))
else:
    print('  Seu IMC é \033[31m{:.2f}\033[m\n  Esta acima de 40.\n  Por isso você tem \033[31mobesidade mórbida\033[m!'.format(imc))
