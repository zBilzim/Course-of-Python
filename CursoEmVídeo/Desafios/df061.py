from ftplib import print_line

n = int(input('Escolha um número: '))
PA = int(input('Escolha a PROGRESSÃO ARITMÉTICA deste número: '))
print(n, end= ('->'))
for c in range(1, 9):
    PA += n
    print(PA, end=('->'))
PA += n
print(PA)