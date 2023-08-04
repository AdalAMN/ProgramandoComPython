valor1 = 45
valor2 = 258.45

#operadores aritméticos
print("Soma:",valor1+valor2)
print("subtração:",valor1-valor2)
print("multiplicação:",valor1*valor2)
print("Divisão:",valor1/valor2)
print(f"Divisão com duas casas decimais: {valor1/valor2:.2f}")
print(f"valor 2: {valor2:.1f}")
#obter dados do teclado (Entrada de dados)
usuario = input("Informe o seu nome: ")
print(f"Seja bem-vindo {usuario}")
idade = int(input("Informe sua idade: "))
print(f"O nome do usuario é {usuario}. Sua idade é: {idade}")
#Mostrar o dobro da idade informada pelo usuario
print(f"O dobro de sua idade é {idade*2}")
#mostrar o tipo de dados da variavel
print("Idade: ",type(idade))
print("Usuario: ",type(usuario))
Valor_curso = float(input('Informe o valor do curso: '))
print(f"O valor do curso é: {Valor_curso}")
#mostrar uma mensagem com 25% do valor do curso
#Parabéns! Você ganhou <valor> de credito na proxima compra
valor = Valor_curso*0.25
print(f"Parabéns! Você ganhou {valor} de credito na proxima compra")
#solicitar quantidade de parcelas do pagamento
Num_parcelas = int(input("Insira o numero de parcelas: "))
#mostrar valor das parcelas sem juros
Valor_parcelas = Valor_curso / Num_parcelas
print(f"O valor será parcelado em {Num_parcelas} parcela(s), onde cada uma irá valer {Valor_parcelas} por mês sem juros")