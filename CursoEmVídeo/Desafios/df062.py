resp = 'S'


n = int(input('Escolha um número: '))
PA = int(input('Escolha a PROGRESSÃO ARITMÉTICA deste número: '))
print(n, end= ('->'))
while resp in 'S SIM':
    for c in range(1, 9):
        PA += n
        print(PA, end=('->'))
    PA += n
    print(PA)
    print(' ')
    resp = input('Quer continuar? ').upper()
