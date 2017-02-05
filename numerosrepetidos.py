num = int(input("Insira um número: "))
ant = -1
repetido = False
resto = 1
while resto > 0 and not repetido:
#    print("num",num)
#    print("resto",resto)
#    print("ant",ant)
    resto = num % 10
    num = num // 10

    if resto == ant:
        repetido = True
    ant = resto
if repetido:
    print("O número", resto,"foi repetido")
else:
    print("Nenhum número repetido encontrado")
