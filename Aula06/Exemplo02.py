#criar uma lista de notas
notas = [6,25,2,10,9,8.8]
#valor máximo de uma nota da lista
print(max(notas))
#Valor mínimo de uma nota de lista
print("Menor valor:",min(notas))
#Quantidade de itens na lista de notas
print("Quantidade de notas",len(notas))
#Soma total das notas da lista
print("Soma das notas:",sum(notas))
#Mostrar média das notas da lista
print(f"Média aritmética: {sum(notas)/len(notas):.2f}")
#Operador in
print(11 in notas)
#loop for com listas
print(notas)
for i in notas:
    print(i,end=" ")
#leia 5 notas utilizando lista e estrutura de repetição
i = 1
valor = 0
lista_de_notas = []
for i in range(5):
    valor = float(input("Insira a nota: "))
    lista_de_notas.append(valor)
    
print("Todas as notas informadas:",lista_de_notas)
print("A quantidade de notas",lista_de_notas)
print("A soma das notas é:",sum(lista_de_notas))

# l1 = [1,2,3,]
# l2 =l1
# l2.append(100)
# print(l1)

#leia uma quantidade de notas determinada pelo usuário e faça a soma dos valores digitados
quantidade = int(input("Indique a quantidade de notas "))
cont = 1
notas3 = []
while cont<=quantidade:
    nume = float(input("Informe a nota: "))
    if nume>+0 and nume<=10:
        notas3.append(nume)
        cont+=1
    else:
        print("Nota invalida")
        continue
print("Total é:", sum(notas3))


