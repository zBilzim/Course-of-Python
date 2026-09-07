n1 = float(input('NOTA DE MATEMÁTICA: '))
n2 = float(input('NOTA DE PORTUGUÊS: '))
media = (n1 + n2) / 2
if media < 5:
    print(f'TIROU \033[:31m{media}\033[m, REPROVADO!! ')

elif (media >= 5) and (media <= 6.9):
    print(f'TIROU \033[:33m{media}\033[m, RECUPERAÇÃO.')

else:
    print(f'TIROU \033[:32m{media}\033[m, PARABÉNS')