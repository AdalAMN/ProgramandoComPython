"""Crie uma função em Python para retornar a área de um retângulo, considere a seguinte fórmula:"""
def area_quad(comp,alt):
    if comp<=0:
        print("Número inválido")
    if alt <=0:
        print("número inválido")

    Area = comp * alt
    print("Área do retangulo:",Area)