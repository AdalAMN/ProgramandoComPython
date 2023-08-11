"""3.	Crie uma lista com os seguintes valores: 
[2,10,30,85,2,6,0,4]
 	- Mostre apenas o terceiro valor
	- Mostre apenas o último valor
- Mostre o dobro de cada valor"""
lista = [2,10,30,85,2,6,0,4]
print("Terceiro valor",lista[2])
print("Último valor",lista[-1])
listaX2 = []
for i in lista:
    listaX2.append(i*2)
print("Dobro de cada numero",listaX2)
