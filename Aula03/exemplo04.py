#Estrutura de repetição While
cont = 0
while cont<=10:
    print(cont, end=" ")
    cont = cont + 1

print("\nValor final do contador:",cont)
#Contagem em 50 até 200
cont = 50
while cont<=200:
    print(cont)
    cont += 50
print("-"*50)
#Contagem iniciando em 10 e finalizando em 80, icrementando os valores de 10 em 10
cont = 10
while cont<= 80:
    print(cont)
    cont += 10
print("-"*50)
#Mostrar a mensagem eu quero estudar 300x
cont = 1
while cont <= 300:
    print("EU QUERO ESTUDAR", end="!!!")
    cont += 1
print("-"*50)
#Leia um numero e mostre a contagem a partir de zero até o numero informado
num = int(input("Insira numero: "))
cont = 0
while cont<=num:
    print(cont)
    cont+=1
print("-"*50)
#Contagem decrescente iniciando em 23 ate 0
cont = 23
while cont >=0:
    print(cont)
    cont-=1
#Leia 2 numeros e mostre a contagem do intervalo dos valores informados
cont = int(input("Insira o valor inicial: "))
num = int(input("Insira o valor limite: "))
cont = cont+1
while  cont < num:
    print(cont)
    cont += 1
