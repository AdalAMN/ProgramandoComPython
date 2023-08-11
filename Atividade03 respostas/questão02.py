#2.	Crie um script que leia o nome de 5 alunos e mostre os dados informados em ordem alfabética
cont = 1
lista = []
while cont <=5:
    nome = input("insira o nome: ")
    lista.append(nome)
    cont+=1
print(sorted(lista))