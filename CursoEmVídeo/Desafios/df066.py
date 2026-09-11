soma = 0
while True:
    n1 = int(input('Digite um número: '))
    if n1 == 999:
        break
    soma += n1
print(f'A soma dos valores é: {soma}')