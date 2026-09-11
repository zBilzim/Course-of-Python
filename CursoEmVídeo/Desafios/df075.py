v = int(input('Digite um valor: '))
v2 = int(input('Digite um valor: '))
v3 = int(input('Digite um valor: '))
v4 = int(input('Digite um valor: '))
valores = (v, v2, v3, v4,)
print('Os valores foram: ', end=' ')
for c in valores:
    print(c,end=' ')
print(f'\nO valor 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O valor 3 aparece na posição: {valores.index(3)+1}')
else:
    print('O valor 3 NÃO aparece na lista.')

print('Os valores Pares foram: ', end=' ')
for c in range(0,4):
    if valores[c] % 2 == 0:
        print(f'{valores[c]}', end=' ')