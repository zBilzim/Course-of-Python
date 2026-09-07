import random
Al1 = input("Digite o nome do 1° Aluno: ")
Al2 = input("Digite o nome do 2° Aluno: ")
Al3 = input("Digite o nome do 3° Aluno: ")
Al4 = input("Digite o nome do 4° Aluno: ")
Sorteio = (Al1 + " " + Al2 + " " + Al3 + " " + Al4).split()
random.shuffle(Sorteio)
print(f"A ordem ficou: {Sorteio}")
