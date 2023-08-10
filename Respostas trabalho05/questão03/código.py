#Crie uma função mostre todos os dados cursos registrados na questão anterior.
try:
    txt = open("questão02/arquivo.txt","a+")
    print("Lendo arquivo...")
    txt.seek(0)
    print(txt.read())
except:
    print("Não consegui achar :.(")