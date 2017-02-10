num = int(input("Digite um inteiro: "))
def fat(num):
    int(num)
    fat=1
    while num > 1:
        fat = fat * num
        num = num - 1
    return fat

while num >= 0:
    print(fat(num))
    num = int(input("Digite um inteiro: "))
