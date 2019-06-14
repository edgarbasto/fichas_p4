#Edgar Basto n.2222
lista = ['Iva', 25, 'Rui', 19, 'Rato', 'abc', 33]

print('a- Imprima toda a lista:')
print(lista)

print('b- Imprima os elementos de 2 a 4 (inclusive)')
print(lista[1:4])

print('c- Imprima os elementos do início até ao elemento 3 (exclusive)')
print(lista[:3])

print('d- Imprima os elementos de 3 até ao fim da lista')
print(lista[2:])

print('e- Crie uma nova lista, chamada lista2, e junte-a à lista1, criando assim uma nova lista. Imprima a nova lista.')
lista2 = ['Um', 'Dois', 'Tres']
print(lista + lista1)
