import random
a = str(input('Digite o Nome do Primeiro Aluno: '))
b = str(input('Digite o nume do Segundo Aluno: '))
c = str (input('Digite o Nome do Terceiro Aluno: '))
d = str(input('Digite o Nome do Quarto Aluno: '))
# podeira criar uma lista tbm fazendo: lista = [a,b,c,d] e criar outra variável
# como: escolhido = randon.choice(lista) e print (escolhido)
al = random.choice([a,b,c,d])

print('O aluno selecionado foi: {}'.format(al))

