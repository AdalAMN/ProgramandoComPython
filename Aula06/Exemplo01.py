#Aula de listas

# coxinha = []
# print(type(lista))

lista = [2,8,10,4,55,'coxinha',34,'maionese',33]
print(type(lista))
print("Primeiro item da lista:",lista[0])
print("Último item da lista:",lista[8])
print("Último item da lista:",lista[-1])
print("Penúltimo item da lista:",lista[-2])
print("Quantidade de itens da lista:",len(lista))
#print("Lista ordenada:",sorted(lista))
pc = ["Mouse","Monitor","HD","Memória Ram","Câmera"]
print(sorted(pc))
lista2 = [6,8,4,11,55,0,3]
print(sorted(lista2))
#mostrar intervalos da lista
print(lista2)
print(lista2[2:5])
print(lista2[3:])
print(lista2[:4])
#adicionar item ao final da lista
lista2.append(1000)
print(lista2)
#inserir item em posição determinada da lista
lista2.insert(2,5000) #.insert(<posição>,<valor>)
print(lista2)
#unir duas listas
lista2.extend(lista)
print(lista2)
#remover ultimo item da lista ou o índice informado
lista2.pop()
print(lista2)
#remover item específico da lista
lista2.remove('coxinha')
print(lista2)
#copiaar referências
lista3 = pc
#copiar objeto
lista4 = pc.copy()
print("print 3", lista3)
print("Lista 4", lista4)
pc.append("SSD")
pc.append("Teclado")
print(lista3)
lista3.append("Placa de Video")
print(lista4)
print(pc)