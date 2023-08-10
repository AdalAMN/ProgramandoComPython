#Crie uma função que leia o nome do curso, carga horária e valor e registre em um arquivo.
try:
    txt = open("questão02/arquivo.txt","+a")
    nome = input("Insira o nome do curso: ")
    carga = int(input("Insira a carga horária do curso: "))
    valor = float(input("Insira o valor do curso: "))
    txt.write(f"{nome}, carga horária de {carga}\nCusto: R${valor}\n{'='*50}\n")
except:
    print("Impossível acessar arquivo!")