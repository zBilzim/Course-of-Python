print("Olá, me chamo Bil e sou o robô do Bilzim!! Quer jogar comigo?")
while True:
    YesorNo = input()
    if YesorNo in ('Sim, sim, s'):
        print('Ótimo ent')
        print("Vamos jogar pedra papel e tesoura. Escolha um.")
        while True:
            PPT = input("")
            if PPT in ("Pedra, pedra, Stone"):
                print("Eu escolho Papel")
                print("Você perdeu. Vamos dnv?")
            elif PPT in ("Tesoura, tesoura"):
                print("Eu escolho Pedra")
                print("Você perdeu. Vamos dnv?")
            elif PPT in ("Papel, papel, paper"):
                print("Eu escolho Tesoura")
                print("Você perdeu. Vamos dnv?")
            break
    elif YesorNo in ('Não, não, nao, Nao, N'):
        print('Babaca.')
        break
    else:
        print('Só pode sim ou não.')
