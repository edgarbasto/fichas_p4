#Edgar Basto n.2222
import os
from pprint import pprint

pprint(os.listdir())

lista_de_palavras_unicas = []
ficheiro = input('Nome do ficheiro a abrir: ') 

try:
	f = open(ficheiro, 'r')  
except:
	print('O ficheiro não exite!')

try:
    conteudo = f.read()
    f.close()
except:
    print('Não foi possivel ler o ficheiro.')  
    quit()

palavras = conteudo.split()
palavras_unicas = set(palavras)
print(palavras)
print(palavras_unicas)

try:
    novo_f = open(ficheiro, 'w')
    novo_f.write(' '.join(palavras_unicas))
    print('O ficheiro foi reescrito com as palavras únicas.')
except:
    print('Não foi possível criar o novo ficheiro.')
