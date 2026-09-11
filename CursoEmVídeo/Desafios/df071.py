sacado = 'S'
tot50 = 50
tot20 = 0
tot10 = 0
tot1 = 0
c = 0
while True:
        saque = int(input('QUANTO VOCÊ QUER SACAR? '))
        tot50 = saque // tot50
        sobra = saque % 50


        print(tot50)
        print(sobra)
        if sobra // 20 != 0:
            tot20 = sobra // 20
            sobra = sobra % 20
            print(tot20)
            print(sobra)
        if sobra // 10 != 0:
                tot10 = sobra // 10
                sobra = sobra % 10

                # print(tot10)
                # print(sobra)

        if sobra // 1 >= 1 or sobra // 1 <= 9:
                    tot1 = sobra // 1
                    sobra = sobra % 1
                    print(sobra)
                    print(tot1)
                    break
        else:
            break

print(f'''{tot50} = 50
{tot20} = 20
{tot10} = 10
{tot1} = 1''')







# elif saque % 20 == 0:
#
# elif saque % 10 == 0:
#
# elif saque % 1 == 0:







    #      sacado = input('Quer fazer outro saque? ').strip().upper()[0]
    #
    # elif sacado == 'N':
    #     break
    # else:
    #     print('APENAS SIM ou NÃO')
    #     sacado = input('Quer fazer outro saque? ').strip().upper()[0]