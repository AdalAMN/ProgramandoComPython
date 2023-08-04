#Operadores Logicos
valor1 = 500
valor2 = 1000
valor3 = 1250
#Operador logico E(and)
print("Verificação do valor 1:",valor1>valor2 and valor1>valor3)
print("Verificação do valor 2:",valor2>valor1 and valor2>valor3)
print("Verificação do valor 3:",valor3>valor1 and valor3>valor2)
#Operador lógico OU(or)
print("Verificação do valor 1:",valor1>valor2 or valor1>valor3)
print("Verificação do valor 2:",valor2>valor1 or valor2>valor3)
print("Verificação do valor 3:",valor3>valor1 or valor3>valor2)
#Operador lofico não(not)
print("Verificação do valor 1:",not(valor1>valor2 or valor1>valor3))
print("Verificação do valor 2:",not(valor2>valor1 or valor2>valor3))
print("Verificação do valor 3:",not(valor3>valor1 or valor3>valor2))
