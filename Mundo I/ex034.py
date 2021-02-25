salario = float(input('Qual é o salário do funcionário: '))

if salario > 1250:
    print('O salário do funcionário teve um aumento de 10%. Totalizando o valor de R$ {:.2f}!'.format(salario*1.10))
else:
    print('O salário do funcionário teve um aumento de 15%. Totalizando o valor de R$ {:.2f}!'.format(salario*1.15))