print('Será que voce pode conseguir um empréstimo para financiar uma casa baseado no valor do seu salário?\nInsira as informações abaixo para descobrir!')
print('-=-' * 15)
casa = float(input('Digite o valor da casa que você deseja comprar: '))
salario = float(input('Digite seu salário mensal: '))
anos = float(input('Digite em quantos anos você deseja pagar a casa: '))

prestacao = casa / (anos * 12)
print('-=-' * 10)
if prestacao < salario * 0.3:
    print('Com esse salário você conseguirá pagar as prestações mensais no valor de R$ {:.2f}!\nEMPRÉSTIMO CONCEDIDO!'.format(prestacao))
else:
    print('Com esse salário você não conseguirá pagar as prestações mensais no valor de R$ {:.2f}!\nEMPRÉSTIMO REPROVADO.'.format(prestacao))