largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
y = 1
while y <= altura:
    x = 1
    while x <= largura:
        print("#",end="")
        x = x + 1
    print()
    y = y +1
