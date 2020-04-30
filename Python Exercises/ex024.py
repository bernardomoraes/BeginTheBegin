#n = input('Digite o nome da cidade: ')
#ns = n.strip().lower().split()
#r = ns[0].find('santo')
#print(r)

#Da pra fazer de outra maneira na linha trocariamos o print e não precisariamos usar tanta variável

n = input('Digite o nome da cidade: ').lower().strip()
print(n[:5] == 'santo')

