num = int(input("Digite um número inteiro: "))
ant = -1
repetido = False
resto = 1
#while resto > 0 and not repetido:
while num > 0 and not repetido:
#    print("num",num)
#    print("repetido",repetido)
    resto = num % 10
    num = num // 10
    if resto == 0 and num == 0:
        resto = 0
        num = 1
        repetido = False

    if resto == ant:
        repetido = True
    else:
        repetido = False
    ant = resto
#    print("-------")
#    print("resto",resto)
#    print("num",num)
#    print("repetido",repetido)
if repetido:
    print("sim")
else:
    print("não")
