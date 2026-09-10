soma = 0
tot = 0
n = int(input('Digite um número: '))
resp = input('Quer continuar? ').upper()
mnr = n
while resp in 'S, SIM':
    n = int(input('Digite um número: '))
    mai = n
    soma += n
    tot += 1
    if n > mai:
        mai = n
    if n < mnr:
        mnr = n
    resp = input('Quer continuar? ').upper()
media = soma / tot

print(f'A média foi: {media}\nO maior é: {mai}\nO menor é: {mnr}')