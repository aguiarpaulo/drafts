def funcao2():
    return print("nome")


def funcao1(funcao):
    return funcao()


result = funcao1(funcao2)
print(result)
