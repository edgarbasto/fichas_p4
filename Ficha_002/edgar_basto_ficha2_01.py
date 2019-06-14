#Edgar Basto n.2222
lista = []
while True:
    try:
        lista.append(int(input('Digite um número: ')))
    except:
        break    
    print('numeros pares introduzidos: ' + str(list(filter(lambda x: x % 2 == 0, lista))))
