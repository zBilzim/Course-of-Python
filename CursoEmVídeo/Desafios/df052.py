for c in range(1,5):
    n = int(input('Digite um valor: '))
    if (n % 1 == 0) and (n % 2 == 1) or (n == 2):
        print(f'{n} é um número primo.')

    else:
        print(f'{n} não é um número primo.')