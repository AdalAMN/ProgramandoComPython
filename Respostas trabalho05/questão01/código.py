#Crie uma função que leia o nome e as notas de um aluno e salve em um arquivo o nome, a média e data do registro.
from datetime import date
data = date.today()
data = data.strftime('%d / %m / %Y')
try:
    txt = open('questão01/arquivo.txt','a+')
    nome = input("Nome do aluno: ")
    nota = float(input("Nota do aluno: "))
    txt.write(f"{nome} -> {nota}\n{data}")
except:
    print("Erro ao acessar o arquivo!")