import random
print('Irei pensar em um número aleatório entre 1 á 10 e você terá que descobrir.')
n = int(input('Digite o número: '))
a = random.randint(1,10)
print(f'Eu escolho: {a}')
if n == a:
    print(f'Parabéns, você acertou.')
else:
    print('Horrível, você errou.')
