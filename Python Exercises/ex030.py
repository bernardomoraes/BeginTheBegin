n = int(input('Digite um número para saber se ele é par ou impar: '))
r = n%2
print(r)
if r != 0:
    print('O número {} é impar!'.format(n))
else:
    print('O número {} é par!'.format(n))