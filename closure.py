def criar_saudacao(saudacao,nome):
    def saudar():
        return f'{saudacao},{nome}'
    return saudar

s1 = criar_saudacao('bom dia','Ana')
s2 = criar_saudacao('boa tarde','joao')

print(s1())
print(s2())