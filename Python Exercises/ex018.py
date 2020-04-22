import math
n= float(input('Digite um ângulo: '))

c = math.cos(math.radians(n))
s = math.sin(math.radians(n))
t = math.tan(math.radians(n))
# lembrar que o python sempre calcula em radianos e para transforamar de radianos para angulo usa a função radians
print('Ângulo: {}º\n'
      'Seno: {:.2f}\n'
      'Cosseno: {:.2f}\n'
      'Tangente: {:.2f}\n'.format(n,s,c,t))
