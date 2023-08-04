"""8.	Crie um script em Python que leia dez números e mostre a média dos valores informados."""
cont = 1
soma = 0
while cont <=10:
    valor=int(input("Insira um numero: "))
    soma = soma + valor
    cont+=1
media = soma/10
print(media)
