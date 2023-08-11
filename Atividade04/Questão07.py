#Crie uma função em Python para retornar a quantidade de itens existentes em um dicionário.
def items(dicio):
    Cont = 0
    for item in dicio.items():
        Cont = Cont + 1
    print(f"Existem {Cont} itens no inventário")