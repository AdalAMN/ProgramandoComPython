#Estrutura de repetição while(Continuação)
#Leia 5 numeros e mostre a soma de todos os valores informados

"""cont = 1
soma = 0 #acumulador

while cont<=5:
    num = float(input("Informe um valor: "))
    soma = soma + num
    cont+=1
print("Resultado da soma é:",soma)
print("="*100)"""
#Calcular a soma dos valores do intervalo(fechado) das variáveis a e b (280)
"""a = 10
b = 25
soma = 0
while a <= 25:
    soma = soma + a
    a+=1
print("Resultado da soma é:",soma)
print("="*100)"""
#Leia 2 valores e mostre a soma do intervalo entre eles
"""Valor1 = int(input("Insira o valor inicial: "))
Valor2 = int(input("Insira o valor final: "))
soma= 0

if Valor1 < Valor2:
    while Valor1 <= Valor2:
        soma = soma + Valor1
        Valor1 +=1
elif Valor2 > Valor1:
    print("Infelizmente não foi possível somar.\nVerifique os valores informados!")
print("Resultado:",soma)
print("="*100)"""
#some 5 valores positivos informados pelo usuario
"""cont =1
soma = 0

while cont<=5:
    valor = int(input("Informe o valor: "))
    if valor<0:
        print("Valor Negativo!!!\nInsira um valor positivo!")
        continue
    else:
        soma = soma+valor
        cont+=1
print("Resultado:",soma)
"""
#some 5 valores negativos informados pelo usuario
"""cont =1
soma = 0

while cont<=5:
    valor = int(input("Informe o valor: "))
    if valor>0:
        print("Valor Positivo!!!\nInsira um valor negativo!")
        continue
    else:
        soma = soma+valor
        cont+=1
print("Resultado:",soma)
"""
#Leia 3 notas e mostre a media, caso seja digitado um valor negativo ou acima de 10 será solicitado um novo valor
cont = 1
soma = 0
media = 0
while cont<=3:
    nota = float(input("Insira a nota para calcular a media: "))
    if nota <0:
        print("ERRO!ERRO!ERRO!ERRO\nTENTE NOVAMENTE")
        continue
    elif nota>10:
        print("Você realmente acha que pode mentir para mim?\nEu sei que a nota máxima é 10 e nada pode ultrapassa isso\n Você deveria sentir vergonha na sua falta de honestidade\n Insira um valor verdadeiro e pare de me fazer perder tempo!")
        continue
    else:
        soma = soma + nota
        cont+=1
media = soma/3
print(f"Media final: {media:.2f}")
if media>7:
    print("Parabéns!! Você foi aprovado!\nEstou muito orgulhoso com você!")
else:
    print("Você foi reprovado, estude mais na próxima vez")