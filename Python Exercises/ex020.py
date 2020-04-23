from random import shuffle
a = input('Digite o nome de um aluno: ')
b = input('Digite o nome de outro aluno: ')
c = input('Digite o nome de outro aluno: ')
d = input('Digite o nome de outro aluno: ')

x = [a,b,c,d]
shuffle(x)
print(x)
