l=float(input('Digite a Largura da Parede: '))
a=float(input('Digite a Altura da Parede'))

area=l*a
t=area/2
print('A quantidade de tinta necessária para pintar uma parede de {:.1f} m² é de {:.1f} litros.'.format(area,t))