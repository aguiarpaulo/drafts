
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]
'''
def ordena(item):
    return item['nome']

lista.sort(key=ordena)
'''

sorted(lista, key=lambda item: item['sobrenome'])
#lista.sort(key=lambda item: item['sobrenome'])

for item in lista:
    print(item)