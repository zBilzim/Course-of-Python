re1 = float(input('Digite o valor da reta: '))
re2 = float(input('Digite o valor da reta: '))
re3 = float(input('Digite o valor da reta: '))
if (re1 + re2 > re3) and (re1 + re3 > re2) and (re3 + re2 > re1):
    print('Estas retas formam um triângulo.')
    if (re1 == re2) and (re2 == re3):
        print('Este triângulo é EQUILÁTERO')

    elif (re1 != re2) and (re2 != re3):
        print('Este triângulo é ESCALENO')

    elif (re1 != re2) or (re1 != re3):
        print('Este triângulo é ISÓSCELES')


else:
    print('Estas retas NÃO formam um triângulo.')