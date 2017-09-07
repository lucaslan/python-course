def soma_elementos(lista):
#lista = [1,2,3,4,5,6,-1]
	somatotal=0
	if not (len(lista) // 2) == 0:
	    impar=True

	for x in range(0,len(lista),2):
	#    print("x=",x)
	    soma1=lista[x]
	    if x == (len(lista)-1):
	        soma2=0
	    else:
	        soma2=lista[(x+1)]
	    soma=soma1+soma2
	    somatotal = somatotal + soma

	return(somatotal)
