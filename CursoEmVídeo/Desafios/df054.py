mni = 0
mai = 0
for c in range(1,8):
    pss = int(input(f'{c}° pessoa nasceu em: '))
    if 2026 - pss < 18:
        mni += 1
    else:
        mai += 1
print(f'MENORES DE IDADE: {mni}')
print(f'MAIORES DE IDADE: {mai}')
