num = int(input("Digite um número: "))

if (num % 3) == 0:
    if (num % 5) == 0:
        print("FizzBuzz")
    else:
      print(num)
else:
    print(num)
