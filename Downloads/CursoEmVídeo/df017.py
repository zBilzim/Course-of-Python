import math
Cto = float(input("Digite o valor do cateto oposto: "))
Cta = float(input("Digite o valor do cateto adjacente: "))
P = (math.pow(Cto, 2) + math.pow(Cta, 2)) ** 0.5
print(f"O comprimento da hipotenusa é: {P}")