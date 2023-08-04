#Aplicar operadores logicos com if
#Leia a qtd de faltas de um aluno e sua media final
qtd_faltas = int(input("Informe a quantidade de faltas: "))
media = float(input("Informe a média final:" ))
#Condições de reprovação
#qtd de faltas maior do que 8 e média menor do que 7
print("Resultado:",qtd_faltas>8 or media<7)
print("*"*50)
if qtd_faltas>8 or media<7:
    print("Aluno Reprovado")
else:
    print("Aluno Aprovado")
#analisar condição do aluno somente se o valor das faltas for maior ou igual a zero
if qtd_faltas >= 0:
    if qtd_faltas > 8 and media<7:
        print("Alunop reprovado por falta e falta de nota")
    elif qtd_faltas > 8 and not(media<7):
        print("Aluno reprovado por falta")
    elif not(qtd_faltas>8) and media<7:
        print("Aluno reprovado por nota")
    else:
        ("Aluno aprovado")
else:
    print("Faltas invalidas")

    

