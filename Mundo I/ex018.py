from math import radians, sin, cos, tan
angulo_1 = float(input('Digite o ângulo: '))
seno = sin(radians(angulo_1))
print('O ângulo {} tem o seno {:.2f}'.format(angulo_1,seno))
cosseno = cos(radians(angulo_1))
print('O ângulo {} tem o cosseno {:.2f}'.format(angulo_1,cosseno))
tangente = tan(radians(angulo_1))
print('O ângulo {} tem a tangente {:.2f}'.format(angulo_1,tangente))