
def zipper(lista1,lista2):
    intervalo = min(len(lista1),len(lista2))
    print(intervalo)
    return [ (lista1[i]+ lista2[i]) for i in range(intervalo)
    ]

l1 = [1,2,3,4,5,6,7]
l2=[1,2,3,4]

print(zipper(l1,l2))