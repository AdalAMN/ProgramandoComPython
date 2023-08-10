try:
    txt = open("dados3.txt","a+",encoding='utf-8')
    nome = input("Informe o nome:")
    email = input("Informe o email:")
    txt.write(f"{nome:^2} - {email:^5}\n")
except:
    print("Erro ao gravar os dados!!!")