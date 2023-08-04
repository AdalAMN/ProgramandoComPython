# leia um numero real e armazene o valor em uma variavel
num = float(input("Informe um numero: "))
print(type(num))
#varificar se o numero informado é positivo
if num>0: #test for true
    print("O valor informado é positivo")
elif num== 0:
    print("O valor informado é neutro")

else: #test for false
    print("O valor informado é negativo")
print("aqui finaliza o script")
print("Teste final")