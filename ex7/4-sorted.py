list = [1,2,3,4,4,3,2,1,2,3,4]

def remove_repetidos(lista):
    MOD=sorted(lista[:])
    MAX=len(MOD)
    FINAL=[]
#    print("list=",MOD)
#    print("MOD=",len(MOD))
    for X in range(0,(MAX-1)):
        N1=MOD[X]
        if not N1 in FINAL:
            FINAL.append(int(N1))
    return FINAL
#print(sorted(list))
print(remove_repetidos(list))

#        N1=MOD[X]
#        if X == len(MOD):
#            N2=N1
#        else:
#            N2=MOD[(X+1)]
#        print("X=",X)
#        print("N1=",N1)
#        print("N2=",N2)
#        if N1 != N2:
#            FINAL.append(MOD[X])
#            print(FINAL)
