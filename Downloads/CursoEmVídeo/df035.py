re1 = float(input('Digite o valor da reta: '))
re2 = float(input('Digite o valor da reta: '))
re3 = float(input('Digite o valor da reta: '))
if (re1 + re2 > re3) and (re1 + re3 > re2) and (re3 + re2 > re1):
    print('Estas retas formam um triângulo.')
else:
    print('Estas retas NÃO formam um triângulo.')