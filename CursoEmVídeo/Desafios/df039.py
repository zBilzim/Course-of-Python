Ano = int(input('Em que ano você nasceu? '))
idade = 2026 - Ano
if (idade) < 18:
    print('Você ainda vai se alistar.')
    print(f'Você tem: {idade}')
    print(f'Faltam: {18 - idade} anos para você se alistar')
elif (idade) == 18:
    print('Já esta na hora de se alistar.')
    print(f'Você tem: {idade}')
else:
    print('Já passou da hora de você se alistar!!')
    print(f'Você tem: {idade}')
    print(f'Você está atrasado em {(idade - 18)} ano!!')
