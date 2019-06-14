#Edgar Basto n.2222
import os
from pprint import pprint

d = {'a': 0, 'e': 0 , 'i':0, 'o':0, 'u':0}

pprint(os.listdir())
ficheiro = input('Nome do ficheiro a abrir: ') 

try:
	f = open(ficheiro, 'r')  
except:
	print('O ficheiro não exite!')


try:
	for letra in f.read():
		if letra in d.keys():
			d[letra] += 1
except:
	print('Não foi possivel ler o ficheiro')
	quit()

f.close()
for vogal in d.keys():
	print(str(vogal) + ': '+ str(d[vogal]))

