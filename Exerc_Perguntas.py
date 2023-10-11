perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
#print(type(perguntas))
for pergunta in perguntas:
    print("Pergunta: ",pergunta['Pergunta'])
    print()

    for i,opção in enumerate(pergunta['Opções']):
        print(f'{i})',opção)
        print()
    print()
    escolha = input("Escolha uma opção:  ")
    print()

    if pergunta['Resposta'] == escolha:3

        print("Você Acertou")
    else:
        print('Você errou!!')

    break

