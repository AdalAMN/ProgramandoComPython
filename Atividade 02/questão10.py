"""10.	Crie um script em Python que leia 5 números e mostre o maior valor e o menor valor informado."""

cont = 1
valorant= 0
valorantmenor = 0
while cont <= 5:
    valor = int(input("Insira um valor: "))
    if cont==1:
        maior = valor
        menor = valor
    if valor>maior:
        maior = valor
    if valor<menor:
          menor=valor  
    cont+=1
print(maior)
print(menor)
