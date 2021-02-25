from math import radians, sin, cos, tan
angulo1 = float(input('Digite o ângulo: '))
seno = sin(radians(angulo1))
print('O ângulo {} tem o seno {:.2f}'.format(angulo1,seno))
cosseno = cos(radians(angulo1))
print('O ângulo {} tem o cosseno {:.2f}'.format(angulo1,cosseno))
tangente = tan(radians(angulo1))
print('O ângulo {} tem a tangente {:.2f}'.format(angulo1,tangente))
