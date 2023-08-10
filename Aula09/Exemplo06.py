#Abertura de um arquivo chamado dados2.txt
#ler o nome de uma pessoa

try:
    
    txt = open("dados2.txt","w+")
    for i in range(1,11):
        nome = input("Nome: ")
        txt.write(f"{i} - Nome:{nome}\n")
except:
    print("ERRO :(")
else:
    txt.seek(0)
    print(txt.read())
    txt.close()