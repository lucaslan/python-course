def primo(x):
    fator = 2
    if x == 2:
        return True

    while x % fator != 0 and fator <= x/2:
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True

def n_primos(x):
    y = 2
    count = 0
    while y <= x:
        if primo(y):
            count = count + 1
        y = y + 1
    return count

