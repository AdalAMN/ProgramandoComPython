#Leia o valor de um produto, caso o valor seja moner do que 100, mostre a seguinte mensagem "você recebeu 5% de desconto", caso o contrario "você recebeu 10% de desconto" 
valor = float(input("Insira o valor do produto: "))
if valor < 100:
    print("você recebeu 5% de desconto")
elif valor > 100:
    print("você recebeu 10% de desconto")