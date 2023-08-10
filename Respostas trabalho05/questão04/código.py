#Pesquise funções/métodos para apagar um arquivo e aplique um exemplo.
import os
if os.path.exists("questão02/arquivo.txt"):
    try:
        os.remove("questão02/arquivo.txt")
        print("Arquivo deletado com sucesso!")
    except:
        print("Impossível deletar arquivo")
else:
    print("O arquivo não existe")
