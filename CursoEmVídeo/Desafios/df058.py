from random import randint
tot = 0
c = 'S'
while c == 'S':
    n = int(input('Digite um número de 1 à 10: '))
    rand = randint(1,10)
    print(rand)
    if n == rand:
        print('Uau, VOCÊ ACERTOU!!')
        if tot > 0:
            print(f'Você precisou de {tot} tentativas para isso')

    else:
        print('nossa, VOCÊ ERROU!!')
        tot += 1


    c = input('Quer continuar?').upper()

