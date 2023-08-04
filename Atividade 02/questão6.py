"""6.	Faça um script em Python para receber dois números informados pelo usuário, mostre o valor da soma de todos os números entre eles e a média dos valores."""
valor1 = int(input("Insira o primeiro valor: "))
valor2 = int(input("Insira o segundo valor: "))
divisor = 0
soma = 0
media = 0
if valor1< valor2:
    while valor1<=valor2:
        divisor +=1
        soma = soma + valor1
        valor1+=1
    media = soma/divisor
    print(media)
elif valor2< valor1:
    while valor2<=valor1:
        divisor +=1
        soma = soma + valor2
        valor2+=1
    media = soma/divisor
    print(media)
