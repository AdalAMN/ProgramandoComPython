"""1.	Crie um script em Python para receber dois números informados pelo usuário e mostrar todos números entre eles em ordem decrescente."""
numero1 = int(input("Insira o primeiro número: "))
numero2 = int(input("Insira o segundo número: "))
if numero1 > numero2:
    while numero1>=numero2:
        print(numero1)
        numero1-=1
elif numero1 < numero2:
    while numero2>=numero1:
        print(numero2)
        numero2-=1
