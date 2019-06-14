#Edgar Basto n. 2222
d = {'Ziggy': 'canario', 'Pluto': 'cao', 'Kitty': 'gato', 'Nemo': 'peixe', 'Mickey': 'rato'}
print(d)

while True:
    nome = input('Nome do animal: ')
    if nome == 'fim':
        break
    animal = input('Éspecie do animal >> ')
    if animal == 'fim':
        break
    d[nome] = animal
print('lista atual: ' + str(d))
print('Animais na base de dados: ' + str(list(d.keys())))
search = input('Procurar animal por nome: ')

if search in d.keys():
    print('O {} é da espécie {}'.format(search, d[search]))
else:
    print('Não existe esse animal.')
