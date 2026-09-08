frase = input('Digite uma frase ')
div = frase.split()
jun = ''.join(div)

if jun.lower() == jun.lower()[::-1]:
    print(frase)
    print('É POLINDROMO')
else:
    print('Não é POLINDROMO')