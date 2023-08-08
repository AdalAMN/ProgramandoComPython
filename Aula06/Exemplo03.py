#Lista compastas
pc = ["Processador","Mouse","Teclado",["memória RAM","HD","SSD"],"Webcam"]
print("Item 1:",pc[0])
print("Item 4",pc[3])
print("Item 4.1:",pc[3][0])
print("Útimo item da sublista:",pc[3][-1])
# print(sorted(pc))
pc[0] = "Fonte"
print(pc)
#Substituir Memória RAM por Memória Flash
pc[3][0]=("Memória Flash")
print(pc)