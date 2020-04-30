f = input('Digite sua frase:\n').strip()
print('Sua frase possui {} letras "a"'.format(f.lower().count('a')))
print('Ela aparece pela primeira vez em {}'.format(f.find('a')+1))
print('Ela aparece pela última vez em {}'.format(f.rfind('a')+1))