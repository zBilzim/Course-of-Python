n1 = int(input('Digite um número: '))
soma = 0
v = 0
aux = n1

c = 0
j = 0
# for c in range(n1,0,-1):
#     if n1 * c == n1:
#         print(f'{n1} x {c} = {n1 * c}')
#     else:
#         print(f'{n1} x {c} = {n1 * c}')
#         n1 = n1 * c
# print(f'O fatorial de {aux} é {n1}')

while c < aux:
    c += 1
    if n1 * c == n1:
        print(f'{n1} x {c} = {n1 * c}')
    else:
        print(f'{n1} x {c} = {n1 * c}')
        n1 = n1 * c