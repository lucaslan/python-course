def maior_elemento(lista):
    maior = -10000000000
    for x in range(0,len(lista),1):
#        print("x=",x)
        x1=lista[x]
        if maior < x1:
            maior = x1

#        print("x1=",x1,"maior=",maior)

    return(maior)

#lista = [-90,-27,-12]
#print(maior_elemento(lista))
