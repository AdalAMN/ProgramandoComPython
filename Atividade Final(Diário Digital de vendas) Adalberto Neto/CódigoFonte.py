escolha = input("Para adicionar um item ao inventario escreva: <adicionar>\nPara ler o inventário escreva: <ler> \n ")
try:
    if escolha == 'adicionar':
        try:
            nome = input("Insira o nome do produto: ")
            valor = float(input("Insira o valor do produto: "))
            quantidade =  int(input("Insira a quantidade: "))
            
        except:
            print("Entrada de valores incorreta!\nTente novamente!")
        try:
            txt = open("dados_produtos.txt","w+")
            txt.write(f"{nome}\nR${valor}\nQuantidade vendida: {quantidade}\n ")
            print("Informações adicionadas com sucesso!")
        except:
            print("Arquivo não encontrado!")
    if escolha == 'ler':
        try:
            txt = open("dados_produtos.txt","a+")
            print("Arquivo encontrado!")
            txt.seek (0)
            print(txt.read())
        except:
            print("Arquivo não encontrado!")
except ValueError:
    print("Escolha uma das opções indicadas!")
