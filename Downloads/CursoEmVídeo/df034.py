sal = float(input('Diga seu salário: '))
if sal > 1251:
    au = sal*1.1
    print(f'Seu salário teve um aumento de 10% ficando: R$ {au:.2f}')
else:
    au = sal*1.15
    print(f'Seu salário teve um aumento de 15% ficando: R$ {au:.2}')