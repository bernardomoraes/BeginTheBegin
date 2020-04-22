#Fazer um programa que calcule a hip a partir do cateto oposto e adjacente
from math import hypot
o = float(input('Digite o Valor do Cateto Oposto: '))
a = float(input('Digite o Valor do Cateto Adjacente: '))

h = hypot(a,o)

print('A hipotenusa do triângulo com catetos adjacente {} e oposto {} é:\nHipotenusa: {}'.format(a,o,h))

