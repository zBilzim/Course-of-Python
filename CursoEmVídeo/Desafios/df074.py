from random import randint
aleatorio = randint(1,9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9)
print('Os valores sorteados foram: ', end='')
for c in aleatorio:
    print(f'{c}', end=' ')
print(f'\nO maior valor foi {max(aleatorio)}')
print(f'O menor valor foi {min(aleatorio)}')
