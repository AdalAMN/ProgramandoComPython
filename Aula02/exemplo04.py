#leia dois numeros inteiros e mostre o menor valor
num1 = int(input("Insira o primeiro numero: "))
num2 = int(input("Insira o segundo numero: "))
if num1==num2:
    print("Voce digitou valorez iguais")
elif num1<num2:
    print(num1)
elif num2 < num1:
    print(num2)
