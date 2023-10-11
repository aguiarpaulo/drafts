'''
def chegada(saudacao,nome):
    print(saudacao,nome)

chegada("Oi","Paulo")

def soma(n1,n2,n3):
    print(n1+n2+n3)
soma(1,2,3)
'''

'''
def percentual(n4, n5):
    print(n4 * (n5 / 100 + 1))


percentual(0, 10)
'''

def fizzbuzz(n1):
    if n1%3 == 0 and n1%5 == 0:
        print('buzzfizz')
    elif n1%5 == 0:
        print('buzz')
    elif n1%3==0:
        print('fizz')
    else:
        print(n1)
    return

result = fizzbuzz(15)
