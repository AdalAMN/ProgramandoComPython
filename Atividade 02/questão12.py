"""12. Faça um script em Python que leia 10 valores positivos e mostre, no final, a soma dos números pares e a soma dos números ímpares. """
cont = 1
somapar = 0
somaimpar = 0
while cont <=10:
    valor = int(input("Insira um valor positivo: "))
    if valor <0:
        print("Insira um valor POSITIVO")
        continue
    else:
        if valor%2==0:
            somapar = somapar + valor
        elif valor%2!=0:
            somaimpar = somaimpar + valor
    cont+=1
print("Soma dos pares:",somapar)
print("Soma dos impares:",somaimpar)
