sompa = 0
for c in range(1,7):
    n = int(input(f'Digite o {c}° número: '))
    if n % 2 == 0:
        sompa += n
print(f'A soma dos PARES é: {sompa}')