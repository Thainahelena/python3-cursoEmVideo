distancia = float(input('Digite a distância da sua viagem em Km: '))

if distancia <= 200:
    distancia = distancia * 0.5
else:
    distancia = distancia * 0.45

print('O preço da sua passagem é: R$ {:.2f}'.format(distancia))