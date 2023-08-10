try: 
    txt = open("dados.txt","a+")
    print("Arquivo encontrado!")
    txt.seek (0)
    print(txt.read())
except:
    print("Problemas ao abrir o arquivo...")