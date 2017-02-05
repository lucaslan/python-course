num = int(input("Digite um número: "))

soma = 0
resto = 1

while resto > 0 :
    resto = num % 10
    num = num // 10
    soma = soma + resto
print("A soma total é:", soma)
