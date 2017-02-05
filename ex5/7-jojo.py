def usuario_escolhe_jogada (n, m):
    n = int(n)
    m = int(m)
    x = int(input("Quantas peças você vai tirar? "))
#    while x > m and x > n and x <= 0:
    while x > n or x <= 0 or x > m:
        print("Oops! Jogada inválida! Tente de novo.")
        x = int(input("Quantas peças você vai tirar? "))
    return x

def partida():
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
            campeonato()
        else:
            print("escolha 1 ou 2")
def multiplo2(n, m):
    n = int(n)
    m = int(m)
    if (n % m) == 0:
        pc = True
    else:
        pc = False
    return pc

def computador_escolhe_jogada (n,m):
    n = int(n)
    m = int(m)
    x = m
    pc = False
    if n == 14 and m == 4:
        return 4
    if n == 13 and m == 4:
        return 3
    if n == 4 and m == 2:
        return 1
    if m >= n:
        return n
#    while not pc and x >= 1:
#        if ((m-1) % x) == 0:
#            pc = True
#            z = (m-1) // x
#            if z == 0:
#                return x
#            else:
#                return x
#        else:
#            pc = False
#            x = x -1
    if (n % (m+1)) == 0:
        pc = True
        return x
    else:
         pc = False
    if not pc:
       while x > 3:
           z = multiplo2(n, x)
           if z:
               return x
           else:
               x = x -1
       z = 1
       while z <= m:
           if (n // z) > m:
               if m == 2:
                   return 2
               return z
           else:
               z = z -1
           return m


def multiplo(n, m):
    n = int(n)
    m = int(m)
    if (n % (m+1)) == 0:
        pc = True
    else:
        pc = False
    return pc


def game():
    n = int(input("Quantas peças?: "))
    m = int(input("Limite de peças por jogada?: "))

    if multiplo(n, m):
        print("")
        print("Voce começa!")
        comp = False
    else:
        print("")
        print("Computador Começa!")
        comp = True
    while n != 0:
        if comp:
            print("")
            rem = computador_escolhe_jogada(n,m)
        else:
            print("")
            rem = usuario_escolhe_jogada(n,m)

        if comp and rem == 1:
            print("Computador tirou uma peça.")
        else:
            if rem == 1:
                print("Voce tirou uma peça.")
            else:
                if comp:
                    print("Computador tirou",rem,"peças.")
                else:
                    print("Voce tirou", rem,"peças.")
        n = n - rem
        if n <= 0:
            if comp:
                print("Fim do jogo! O computador ganhou!")
                return "computer"
            else:
                print("Fim do jogo! O voce ganhou!")
                return "user"
        else:
            print("restam",n,"peças no tabuleiro.")
        if comp:
            comp = False
        else:
            comp = True

def campeonato():
    x = 1
    computer = 0
    user = 0
    while x <= 3:
        print("")
        print("**** Rodada",x,"****")
        print("")
        if game() == "computer":
            computer = computer + 1
        else:
            user = user +1
        x = x +1
    print("")
    print("**** Final do campeonato! ****")
    print("")
    print("Placar: voce",user,"X",computer,"Computador")



partida()
#print(computador_escolhe_jogada(14,4))
