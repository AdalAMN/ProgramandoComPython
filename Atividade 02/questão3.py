"""3.	Faça um script que mostre os números pares em um intervalo definido pelo usuário."""
valor1 = int(input("Insira o valor inicial: "))
valor2 = int(input("Insira o valor final: "))
if valor1 < valor2:
    while valor1<=valor2:
        if valor1%2==0:
            print(valor1)
        valor1+=1
if valor1 > valor2:
    while valor2<=valor1:
        if valor2%2==0:
            print(valor2)
        valor2+=1
    
    
            