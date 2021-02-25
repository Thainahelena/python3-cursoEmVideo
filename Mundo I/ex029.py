velocidade = float(input(('Em que velocidade o carro passou?: ')))

if velocidade > 80:
    print('O carro foi multado por ultrapassar a velocidade de 80Km/h! O valor da multa é de R$ {}!'.format(((velocidade-80)*7)))
else:
    print('O carro estava dentro da velocidade!')