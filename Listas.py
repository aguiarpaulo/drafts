String = 'O Brasil é penta'
lista = String.split(' ')
print(lista)

for indice, valor in enumerate(lista):
    print(indice,valor)
    break


lista = ['ana','joao','paulo',1,'2',2,34]

n1,n2,*outra_lista = lista
print(n1,n2, *outra_lista)