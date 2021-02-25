dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))
km = float(input('Digite a quantidade de km que o carro percorreu: '))

print(' Ao ser alugado por {} dias e percorrido {} Km.\n O preço final do aluguel do carro e de R$ {}!'.format(dias,km,((dias*60)+(km*0.15))))