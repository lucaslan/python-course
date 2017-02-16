def maior_elemento(lista):
    maior = 0
    for x in range(0,len(lista),1):
        print("x=",x)
        x1=lista[x]
        if maior < x1:
            maior = x1

        print("x1=",x1,"maior=",maior)

    return(maior)

#lista = [1000,2,20,4,5,6,-1,400]
#print(maior_elemento(lista))
