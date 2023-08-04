"""9.	Crie um script em Python que leia 5 números e mostre o maior valor informado."""
maior = 0
cont = 1
valorant= 0
while cont <= 5:
    valor = int(input("Insira um valor: "))
    if valor>valorant:
        maior = valor
        valorant = valor
    cont+=1
print(maior)