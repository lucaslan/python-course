num = int(input("Digite um número inteiro: "))

soma = 0
resto = 1

while num > 0 :
    resto = num % 10
    num = num // 10
    soma = soma + resto
print(soma)
