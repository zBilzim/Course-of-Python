from random import randint, choice
soma = 0
tot = 0
while True:

    n = int(input('Digite um número: '))
    bot = randint(1, 10)
    soma = n + bot
    ip = ' '
    while ip not in 'IP':
        ip = input('Par ou Impar?[P/I] ').strip().upper()[0]
        print()
    print(f'Escolhi {bot}, deu: {soma}')
    print('DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')
    if ip == 'P':
        if soma % 2 == 0:
            print('VOCÊ GANHOU')
            tot += 1
        else:
            print('VOCÊ PERDEU')
            break


    elif ip == 'I':
        if soma % 2 == 1:
            print('VOCÊ GANHOU')
            tot += 1
        else:
            print('VOCÊ PERDEU')
            break
print(f'TOTAL DE VITÓRIAS: {tot}')











    # if soma % 2 == 0:
    #     np = 'P'
    # else:
    #     np = 'I'
    # tot += 1
    # print(f'Eu escolhi: {bot}')
    # print(f'Deu {soma} que é {ip}')
    # print('VOCÊ GANHOU!!')
    # if ip != np:
    #     print(f'Você perdeu.')
    #     print(f'Vitórias: {tot}')
    #     break


    #ERROS
#     print(f'Eu escolhi {bot} e você escolheu {n}')
#     soma = n + bot
#     if np == ip:
#     print(f'A soma deu: {soma}')
#     print(f'VOCÊ GANHOU. {n} + {bot} = {soma}. isso é {np}')
#     tot += 1
#     n = int(input('Digite um número: '))
#
#         else:
#             print(f'A soma deu {soma} que é: {ip}')
#             print('VOCÊ PERDEU.')
#             break
#
# print(f'TOTAL DE VITÓRIAS CONSECUTIVAS: {tot}')