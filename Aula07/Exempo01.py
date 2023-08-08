alunos = {}
#mostrar primeiro item do dicionario
print(alunos[111])
#mostrar spmente as chaves do divionario
print(alunos.keys())
#mostrar somente os valores armazenados
print(alunos.values())
# Mostrar todos os item do dicionario
print(alunos.items())
#Atualizar dicionario
alunos.update(({555:"Paulo Coelho"}))
print(alunos)
alunos[666] = "Teste"
print(alunos)
alunos[111] = "Carlos da Silva"
print(alunos)
#Exclui um item do dicionario
alunos.pop(666)
print(alunos)
#Mostrar somente os valores do dicionario
for i in alunos.values():
    print(i)
#Mostrar somenete as chaves do dicionario
for i in alunos.key():
    print(i)
#Mostrar todos os items
for i in alunos.items():
    print(i)

for i,j in alunos.items():
    print(i,j,sep=" - ")

dados = {
    'lista_a':[1,2,2,5,8],
    'lista_b':[10,20,30,40],
    'lista_c':[100,200,300,400]
}
print(dados)
print(type(dados))
#Mostrar o ultimo item da lista b
print(dados["lista_b"][-1])