n = float(input('Serão quantos Km de viagem? '))
if n <= 200:
    v = n * 0.50
    print(f'O valor da passagem será: {v}')
else:
    v = n * 0.45
    print(f'O valor da passagem será: {v}')
print('Boa Viagem!!')