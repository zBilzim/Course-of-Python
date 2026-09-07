v = int(input('Digite a velocidade em Quílometros: '))
if v > 80:
    m = float(v - 80) * 7
    print(f'Você foi mutado em: R$ {m:.2f}')
else:
    print('Tudo nos conformes, parabéns.')