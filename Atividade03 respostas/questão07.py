#7.	Crie um script que leia dez números positivos e armazene os dados em uma lista, mostre os dados em ordem crescente, o maior valor informado e menor valor informado.
cont = 1
lista = []
maior = 0
menor = 0
while cont <=10:
    num = float(input("Insira o valor: "))
    if num > 0:
        lista.append(num)
    else:
        continue
    if cont==1:
        maior = num
        menor = num
    if num>maior:
        maior = num
    elif num<menor:
        menor = num
    cont+=1
print("Lista em ordem crescente:",sorted(lista))
print("Maior valor:",maior)
print("Menor valor:",menor)
       
        
