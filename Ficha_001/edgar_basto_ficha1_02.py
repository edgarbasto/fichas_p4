#Edgar Basto n. 2222
numeros = [1, 5, 3, 6, 22, 45, 63, 30, 344, 22, 12, 25, 10]
print('Comprimento da lista: ', len(numeros))
print('Valor maximo da lista:', max(numeros))
print('Valor minimo da lista:', min(numeros))

print('c) Acrescenta ao final da lista os elementos da lista:')
numeros += [21, 53, 23, 54, 22, 2, 1, 13]
print(numeros)

print('d) Altera a lista numeros por forma a que fique ordenada.')
numeros.sort()
print(numeros)


print('e) Indica qual o elemento que aparece mais, indicando o índice da primeira ocorrência na lista.')
print(max(set(numeros), key=numeros.count))

print('f) Imprime os elementos da lista numa só linha e separados por “-”.')
print(str(numeros).join('-'))

print('g) Imprime os elementos de índice ímpar.')
print(numeros[1::2])

print('h) Imprime os elementos que são múltiplos de 5.')
print([num for num in numeros if num % 5 == 0])
