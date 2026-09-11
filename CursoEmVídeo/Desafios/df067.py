while True:
    n = int(input('Digite um número: '))
    if n < 0:
        break
    print(f'A TABUADA DE \033[:32m{n} \033[mé:')
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')






print('NÃO PODE NÚMEROS NEGATIVOS.')