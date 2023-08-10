#mostrar exceção ao digitar números negativos

n = float(input("Informe um valor positivo"))
if n<0:
    raise ValueError("número negativo >:^(")