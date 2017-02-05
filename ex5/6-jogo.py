def inicio(n,m):
    ## n = numero de peças
    ## m = numero maximo de peças que podem ser retiradas
    n = int(n)
    m = int(m)
    if (n % (m+1)) == 0:
        pc = True
    else:
        pc = False

    return pc

def main ():
    print("")
    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("")
    print("1 - para jogar uma partida isolada")
    escolha = int(input("2 - para jogar um campeonato " ))

    if escolha == 1:
        print("Voce escolheu partida isolada")
        game()
    else:
        if escolha == 2:
            print("Voce escolheu campeonato!")
        else:
            print("escolha 1 ou 2")


def game():
    n = int(input("Quantas peças?: "))
    m = int(input("Limite de peças por jogada?: "))

    if not inicio(n,m):
        print("Computador começa!")
        game_2("Computador",n,m)
    else:
        print("Voce começa!")
        game_2("Voce",n,m)



def game_2(name,n,m):


   while 0 < n :
       if name == "Computador":
           if inicio(n ,m)
           ret = m
       else:
           ret = int(input("Quantas peças você vai tirar? "))
           while ret > m:
               print("Jogada inválida! Tente de novo.")
               ret = input(print("Quantas peças você vai tirar? "))
       n = n - ret
       if ret == 1 and name == "Computador":
           print("O computador tirou uma peça.")
       else:
           if ret == 1:
               print("Voce tirou uma peça.")
           else:
               print(name,"tirou",ret,"peças.")

       print("restam",n,"peças no tabuleiro.")

       if name == "Computador":
           name = "Voce"
       else:
           name = "Computador"
   if name == "Computador":
       return "Fim do jogo! Voce ganhou!"
   else:
       return "Fim do jogo! Computador ganhou!"


main()
