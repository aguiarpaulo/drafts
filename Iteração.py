
"""
l2 = list(range(0,100,8))
print(l2)

l3 = ['','fr',45,10.5,True]
for elem in l3:
    print(f'Para cada {elem}, o tipo dele é {type(elem)}')
"""

palavra = "cadeira"
digitada = []
chances = 3

while True:
    if chances < 0:
        print('')
        print(f'Que ruim!! kkkkk Você perdeu!!🤦‍ ')
        print('')
        break

    letra = input('Digite uma letra: ')

    if len(letra)>1:
        print('')
        print('Valor inválido')
        print('')
        continue
    digitada.append(letra)

    if letra in palavra:
        print('')
        print(f'Parabéns a palavra tem a letra "{letra}"')
        print('')
    else:
        print('')
        print(f'Que pena a palavra não tem a letra {letra}')
        print('')
        digitada.pop()

    # print(digitada)

    palavra_temp = ''
    for letra_palavra in palavra:
        if letra_palavra in digitada:
            palavra_temp = palavra_temp + letra_palavra

        else:
            palavra_temp = palavra_temp + '*'

    if palavra_temp == palavra:
        print('')
        print(f'Parabéns!! Você acertou! A palavra é {palavra_temp} 😃😜😜😜🎊🎇🎆')
        print('')
        break
    else:
        print('')
        print(f'A palavra está em {palavra_temp}')
        print('')
    if letra not in palavra:
        chances = chances - 1

