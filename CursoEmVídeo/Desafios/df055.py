mai = 0
mnr = 500
for c in range(1,6):
    pss = int(input(f'{c}° Pessoa Pesa: '))
    if mai < pss:
        mai = pss

    elif mnr > pss:
        mnr = pss
print(f'MENOR PESO: {mnr}')
print(f'MAIOR PESO: {mai}')