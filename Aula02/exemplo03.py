#leia a idade do usuario e informe se ele é maior ou menor de idade
idade = 19#int(input("Insira sua idade: ")) 

if idade <0:
    print("Idade invalida\nVerifique o valor informado.")
else:
    if idade >= 18:
        print("Você é maior de idade")
    else:
        print("Você é menor de idade")