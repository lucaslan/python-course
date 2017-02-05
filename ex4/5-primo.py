num = int(input("Digite um número inteiro: "))

resto = num % 2

if resto != 0:
    resto = num % 3
    if resto != 0:
        print("primo")
    else:
        print("não primo")
else:
    print("não primo")
