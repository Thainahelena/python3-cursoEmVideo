largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

parede = largura * altura
tinta = parede/2
print(' Sua parede tem a dimensão de {} x {} e sua área é de {} m². \n A quantidade de tinta necessária para pintá-la é: {} l/m²!'.format(largura,altura,parede,tinta))