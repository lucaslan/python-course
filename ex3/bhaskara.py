import math
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b ** 2 -4 * a * c

if delta < 0:
    print("esta equação não possui raízes reais")
else:
    r1 = ( -b + math.sqrt(delta) / (2 * a))
    if delta == 0:
        print("a raiz desta equação é", r1 )
    else:
        r2 = ( -b - math.sqrt(delta) / (2 * a))
        if r1 > r2:
            f1 = r1
            f2 = r2
            print("entrou if r1",r1 ,"r2",r2)
        else:
            f1 = r2
            f2 = r1
            print("entrou else r1",r1 ,"r2",r2)
        print("as raízes da equação são", f1,"e",f2)

