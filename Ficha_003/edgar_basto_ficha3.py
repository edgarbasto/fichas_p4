#Edgar Basto n.2222
import re
frase = input('Digite uma frase: ')
palavras = frase.split()
d = {palavras: [p.start() for p in re.finditer(r'\b'+palavras+r'\b', frase)] for palavras in frase.split()}
print(d)
print('\n')
output = ''
a = []
for item in d.keys():
    for x in d[item]:
        a.append((x, item))
a.sort()
output = ' '.join(item[1] for item in a)
print(output)
