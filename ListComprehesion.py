'''
lista = []
for numero in range(10):
    lista.append(numero)
print(lista)

lista2 = [2 * numero for numero in range(10)]
print(lista2)
'''
produtos = [
    {'nome': 'p1', 'preco': 30},
    {'nome': 'p2', 'preco': 40},
    {'nome': 'p3', 'preco': 10},
    {'nome': 'p4', 'preco': 20},
]

novos_produtos = [
    {**produto, 'preco' : produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

print(*novos_produtos,'\n')



