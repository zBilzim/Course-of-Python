p = float(input('Digite seu peso: '))
a = float(input('Digite sua altura: '))
IMC = p / (a*a)
if IMC < 18.5:
    print('Abaixo do peso')
elif IMC <=24.9:
    print('Peso normal')
elif IMC <=29.9:
    print('Sobrepeso')
elif IMC <=40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
