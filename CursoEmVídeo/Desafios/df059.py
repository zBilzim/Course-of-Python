import random
import os
n1 = ""
n2 = ""
aux = '-'
aux2 = '-'
resp = 'S'
while resp in 'S SIM':
    if (n1 != aux) and (n2 != aux2):
        n1 = int(input('Digita um valor: '))
        n2 = int(input('Digite outro valor: '))
    print(f'VALORES: {n1} e {n2}')
    os.system('cls')
    print('''            ======CALCULADORA======
            ==[1] SOMAR          ==
            ==[2] MULTIPLICAR    ==
            ==[3] MAIOR          ==
            ==[4] NOVOS NÚMEROS  == 
            ==[5] SAIR           ==
            =======================''')

    calc = int(input('Escolha entre: 1 à 5: '))
    if calc == 1:
        soma = n1 + n2
        print(f'SOMA: {soma}')
    elif calc == 2:
        mult = n1 * n2
        print(f'MULTIPLICAÇÃO: {mult}')
    elif calc == 3:
        if n1 > n2:
            mai = n1
            print(f'MAIOR {mai}')
        else:
            mai = n2
            print(f'MAIOR {mai}')
    elif calc == 4:
        aux = random.randint(1,10)
        aux2 = random.randint(1,10)
        print(f'{n1} passou a ser {aux}.')
        print(f'{n2} passou a ser {aux2}.')
        n1 = aux
        n2 = aux2

    elif calc == 5:
        resp = 'N'

    if calc != 5:
        resp = input('Quer continuar? ').upper()
print('==================')
print('    OBRIGADO💖    ')
print('==================')



