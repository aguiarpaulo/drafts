while True:
    num_1 = input('Selecione um número:')
    num_2 = input('Selecione outro número')
    operator = input('Selecione um operador:')
    sair = input('Deseja sair? ')

    if sair == 'sim':
        break

    if not num_1.isnumeric() or not num_2.isnumeric():
        print("Valores inválidos!!")
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operator == '+':
        x = num_1 + num_2
        print(x)
    elif operator == '-':
        x = num_1 - num_2
        print(x)
    elif operator == '*':
        x = num_1 * num_2
        print(x)
    elif operator == '/':
        x = num_1 / num_2
        print(x)
    else:
        print("operador inválido!!")