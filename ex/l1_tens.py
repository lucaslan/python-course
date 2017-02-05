num = int(input("Digite um número inteiro: "))

milhar = num // 1000
milhar_rest = num % 1000

centena = milhar_rest // 100
centena_rest = milhar_rest % 100

dezena = centena_rest // 10

print("O dígito das dezenas é", dezena)
