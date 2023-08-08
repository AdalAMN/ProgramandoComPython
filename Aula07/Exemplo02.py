#Operações sobre lista ()
lista = [10,20,5,50,100,6]
#criar umanova lista com o dobro dos valores da lista anterior
lista2 = []
for i in lista:
    lista2.append(i*2)
print(lista2)
lista3 = [i*2 for i in lista]
print(lista3)
#criar uma nova lista com a metade dos valores da lista
lista4 = [1/2 for i in lista]
print(lista4)
#Criar uma nova lista com valores acima de 10, com base nos itens da lista
lista5 = [i for i in lista if i>10]
print(lista5)