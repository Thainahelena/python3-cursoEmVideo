medida = float(input('Digite uma distância em metros: '))
centimetros = medida * 100
milimetros = medida * 1000

print(' A medida que você digitou é: {} m\n Em centrímetros esta medida é: {:.2f} cm\n Em milímetros esta medida é: {:.2f} mm'.format(medida, centimetros, milimetros))