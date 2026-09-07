n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A sua média foi {m:2}')
if m >= 6.0:
    print('Média boa')
else:
    print('Média horrível')

