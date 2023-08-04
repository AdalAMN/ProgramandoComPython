#Estrutura de decisão(Condicionais)
"""Leia a idade do aluno e defina sua categoria de acordo com as seguntes
informações: 
sem categoria - menor do que 3
Intfantil - 3 até 10
Juvenil - 11 até 17
adulto - 18 até 39
senior - 40 até 130
acima de 130 - idade invalida
"""
idade = int(input("Informe a idade do aluno:"))

if idade < 3:
    print("Aluno sem categoria definida")
elif idade <= 10:
    print("Aluno da categoria infantil")
elif idade <= 17:
    print("Aluno da categoria juvenil")
elif idade <= 39:
    print("Aluno da categoria adulto")
elif idade <= 130:
    print("Aluno da categoria senior")
elif idade > 130:
    print("Aluno com idade invalida")