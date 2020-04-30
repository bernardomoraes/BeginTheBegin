vel = int(input('Digite a velocidade do Carro: '))
if vel <= 80:
    print('Você está dentro do limite de velocidade.')
else:
    print('Você foi multado!!')
    print('O valor da multa é de {} reais'.format((vel-80)*7))