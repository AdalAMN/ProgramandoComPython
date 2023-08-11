"""3.	Crie uma função em Python para mostrar o produto da multiplicação entre n valores."""
def multi_valores(n,val):
    i=1
    multi = 1
    while i <= n:
        multi = multi * val
    print(multi)
