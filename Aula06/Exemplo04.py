#tupla

cidades = ("Manaus","Coari","Parintis","Manacapuru")
print(type(cidades))
#mostrar o último item da tupla
print(cidades[-1])
#mostrar o primeiro item da tupla
print(cidades[0])
#mostrar itens ordenados
print(sorted(cidades))
print(cidades.count("Manaus"))

#Leia 3 números positivos e armazene os dados em uma lista, mostre os dados em ordem crescente, o maior valor informado e menor valor informado
i = 1
listA = []
while i <=3:
    valor = int(input("Insira o valor: "))
    if valor < 0:
        continue
    listA.append(valor)
    i +=1
print("Lista ordenada:",sorted(listA))
print("Maior valor:",max(listA))
print("Menor valor:",min(listA))




