print('\033[:32m='*20)
print(' '*6 + '\033[1:34mCADA\033[33mSTRO' + '\033[m '*6)
print('\033[32m='*20)
resp = 'S'
mai = 0
homem = 0
mulher = 0
while True:
    if resp in 'S':
        i = int(input('\033[mIDADE: '))
        s = input('SEXO: [F/M]').strip().upper()[0]
        if i > 18:
            mai += 1
        if s == 'M':
            homem += 1

        if s == 'F' and i < 20:
            mulher += 1
        print(homem)
        print(mai)
        print(mulher)
        resp = input('Quer continuar? ').strip().upper()[0]

    elif resp in 'N':
        break

    else:
        print('Apenas SIM ou NÃO.')
        resp = input('Quer continuar? ').strip().upper()[0]

print('='*20)
print('='*17 + 'TOTAL' + '='*16)
print('='*20)
print(f'PESSOAS +18: {mai}')
print(f'HOMENS: {homem}')
print(f'MULHERES -20: {mulher}')