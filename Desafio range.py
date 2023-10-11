'''
0  10
1  9
2  8
...

lista = ''
for n in range(10,0,-1):
    lista = lista + str(n)
    #print(lista)
    #sequencia = lista.split(' ')
    seq = list(lista)
    print(seq)
for n1, n2 in enumerate(seq):
    print(n1,n2)
'''
for r,n in enumerate(range(10,1,-1)):
    print(r,n)