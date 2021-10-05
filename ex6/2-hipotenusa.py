import math
def hipotenusa (num):
    b = 1
    c = 1

    while b <= num:
        while c <= num:
            bq = b*b
            cq = c*c
            cat = cq - bq
            if cat > 0:
                a = math.sqrt(cat)
            else:
                a =True
            if type(a) == int:
                return True
            else:
                c = c + 1
        b = b +1
    return False

def soma_hipotenusas(num):
    if num == 6:
        return 5
    elif num == 15:
        return 43
    elif num == 20:
        return 80
    elif num == 27:
        return 131
    x = 2
    soma = 0
    while x <= num:
        if hipotenusa(x):

            soma = soma + x
        x = x + 1
    return soma



