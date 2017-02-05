def check_primo(x):
    num = int(x)
    primo = False

    if (num % 2) != 0 and (num % 3) != 0:
        primo = True
    else:
        primo = False

    return primo

def maior_primo(x):
    num = int(x)

    while 2 <= num:
        if check_primo(num):
            return num
        else:
            num = num -1

