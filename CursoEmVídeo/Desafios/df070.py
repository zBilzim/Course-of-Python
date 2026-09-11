resp = 'S'
tot = 0
m1k = 0
mnr = None
barato = None
while True:
    if resp == 'S':
        nome = input('NOME: ')
        valor = int(input('PREÇO: '))
        tot += valor
        if valor > 1000:
            m1k += 1
        if mnr == None:
            mnr = valor
        elif valor < mnr:
            mnr = valor
            barato = nome
        resp = input('CONTINUE? ').strip().upper()[0]
    elif resp == 'N':
        break
    else:
        print('APENAS SIM ou NÃO.')
        resp = input('CONTINUE? ').strip().upper()[0]
print(f'TOTAL GASTO: R${tot}')
print(f'+ DE 1000: {m1k}')
print(f'MAIS BARATO: {barato}')