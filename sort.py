'''

lista = [
    ['p1',33],
    ['p2',43],
    ['p3',2],
    ['p4',7],
    ['p5',9]
]
def func(item):
    return item[1]

lista.sort(key=func, reverse=True)
print(lista)
OR
'''
lista = [
    ['p1',33],
    ['p2',43],
    ['p3',2],
    ['p4',7],
    ['p5',9]
]

lista.sort(key = lambda item: item[1],reverse = True)
print(lista)