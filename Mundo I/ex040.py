print('Bem-Vindo ao programa de calculo de médias! Insira suas notas para saber o status da sua aprovação.')

print('-=-' * 15)
nota_1 = float(input('Digite sua primeira nota: '))
nota_2 = float(input('Digite sua segunda nota: '))
print('-=-' * 15)
media = ((nota_1 + nota_2) / 2)

if media < 5.0:
    print('\033[31mREPROVADO!\033[m Média: {:.1f}'.format(media))
elif 5.0 <= media <= 6.9:
    print('\033[33mRECUPERAÇÃO!\033[m Média: {:.1f}'.format(media))
else:
    print('\033[36mAPROVADO!\033[m Média: {:.1f}'.format(media))