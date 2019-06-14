#Edgar Basto n.2222
from statistics import mean
valor = [float(input('Digite a próxima temperatura:')) for val in range(0,5)]
print('Média das temperaturas introduzidas: ' + str(mean(valor)))