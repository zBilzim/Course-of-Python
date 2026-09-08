soma = 0
mai = 0
mns = 0
for c in range(1,5):
    n = input(f'Digite o {c}° NOME: ')
    i = int(input(f'Digite a IDADE: '))
    s = input(f'Digite o SEXO[M/F]: ')

    soma += i
    if s == 'M' and mai < i:
        mai = i
        vel = n
    if s == 'F' and i < 20:
        mns += 1
media = soma / 4
print(f'A média de idade é: {media}')
print(f'O homem mais velho tem {mai} e se chama: {vel}')
print(f'O total de mulheres com menos de 20 é: {mns}')
