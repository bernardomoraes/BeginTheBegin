km=float(input('Qual a quantidade de Km percorridos pelo carro?\n'))
d=float(input('Qual a quantidade de Dias que o carro foi alugado?\n'))

p=(d*60)+(km*0.15)

print('O preço a pagar é R${:.2f}'.format(p))
