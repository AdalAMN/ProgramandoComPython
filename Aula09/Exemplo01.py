#Ler dois numeros e executar a divisão dos valores
try:
    n1 = float(input("Informe o numerador: "))
    n2 = float(input("Informe o denominador: "))
    print(f"O resultado da divisão é {n1/n2:.2f}")
except ValueError:
    print("O Valor esta incorrento!!!")
except ZeroDivisionError:
    print("Houve um problema ao executar a divisão...")