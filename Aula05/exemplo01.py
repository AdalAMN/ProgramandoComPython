#Exemplo da função range()
# print(list(range(2,20)))
# print(list(range(10)))
# print(range(10))
# print(list(range(10,100,5)))
# print('-'*50)
#loop for
# for i in range(10):
    # print(i, end=" ")
# print("Valor final do contador:",i)
# print('-'*50)
#contagem de 20 at´1 30 usando laçco for
# for j in range(20,31):
    # print(j, end=" ")
# print("")
# print('-'*50)
#contagem 10 até zero usando o laço for
# for k in range(10,-1,-1):
    # print(k,end=" ")
#leia 5 numeros inteiros e mostre uma mensagem quando o numero for par
# for l in range(5):
    # num = int(input("Informe o valor: "))
    # if num%2==0:
        # print("Esse é um número par")
#Leia 5 números e some somente os valores ímpares
soma = 0
cont = 0
for m in range(5):
    num = int(input("Informe o valor: "))
    if num%2!=0:
        soma = soma + num
        cont+=1
print(soma)
print(cont)
#Mostre a média aritmética dos ímpares
print(f"A média de impares é {soma/cont:.2f}")