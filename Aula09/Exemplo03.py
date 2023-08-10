#Ler a idade de um funcionario e tratar possíveis números negativos ou valores acima de 130
idade = int(input("Informe a idade: "))

if idade>0 and idade<130:
    print("Sua idade é:",idade)
else:
    raise Exception("Valor informado está incorreto")
