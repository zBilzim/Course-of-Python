nasc = int(input('Digite seu ano de nascimento: '))
idade = 2026 - nasc
if idade <= 9:
    print('Você é MIRIM')

elif idade <= 14:
    print('Você é INFANTIL')

elif idade <= 19:
    print('Você é JUNIOR')

elif idade == 20:
    print('Você é SÊNIOR')


else:
    print('Você é MASTER')