num = int(input("Digite um número: "))
num_array = []
while num > 0:
    num_array.append(num)
    num = int(input("Digite um número: "))

xd = []
#print("tamanho:",len(num_array))
maximo = len(num_array) - 1
for x in range(maximo,-1,-1):
#    print("x=",x,"maximo=",maximo)
#    print(num_array[x])
    xd.append(int(num_array[x]))

print(xd)
