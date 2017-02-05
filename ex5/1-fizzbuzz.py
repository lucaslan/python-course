def fizzbuzz(x):
    y=int(x)
    if (y % 3) == 0 and (y % 5) == 0:

       out ="FizzBuzz"
    else:
        if (y % 3) == 0:
            out = "Fizz"
        else:
            if (y % 5) == 0:
                out = "Buzz"
            else:
                out = y
    return out

