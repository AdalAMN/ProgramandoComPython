"""4.	Faça um script que leia dois valores positivos e mostre a soma dos números ímpares entre eles."""
valor1 = int(input("Insira o primeiro valor: "))
valor2 = int(input("Insira o segundo valor: "))
if valor1>0 and valor2>0:
    if valor1 < valor2:
        while valor1<=valor2:
            if valor1%2!=0:
                print(valor1)
            valor1+=1
    elif valor2 < valor1:
        while valor2<=valor1:
            if valor2%2!=0:
                print(valor2)
            valor2+=1
else:
    print("Um dos números é negativo\nInsira um valor positivo")