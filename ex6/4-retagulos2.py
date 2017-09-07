largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
y = 1
while y <= altura:
    x = 2
    print("#",end="")
    if y == 1 or altura == y:
        z = 1
        while z < largura:
            print("#",end="")
            z = z +1
    else:
        z = 2
        while z < largura:
            print(" ",end="")
            z = z +1
        print(end="#")
#####################################
    while x < altura:
        if x == 1 or largura == x:
            print("#",end="")
        else:
            print(end="")
        x = x + 1

    print("")
    y = y +1



