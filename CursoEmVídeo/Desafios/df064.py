fim = 998
tot = 0
soma = 0
n1 = ''
while n1 != '999' :
    n1 = int(input('Escreva o primeiro número: '))
    if n1 != 999:
        tot += 1
        soma += n1
    n1 = str(n1)
print(f'O total foi: {tot}')
print(f'A soma foi: {soma}')