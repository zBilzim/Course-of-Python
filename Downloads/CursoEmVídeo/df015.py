D = int(input("Por quantos dias foi alugado? "))
Km = float(input("Quantos Quilometros foram percorridos? "))
D = D * 60
Km = Km * 0.15
Tot = Km + D
print(f"A quantidade a ser de aluguel a ser pago é R${Tot}.")