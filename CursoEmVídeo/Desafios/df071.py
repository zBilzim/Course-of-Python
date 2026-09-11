tot50 = 50
tot20 = 0
tot10 = 0
tot1 = 0
c = 0
print('='*21)
print('  MÁQUINA DE SAQUE')
print('='*21)
while True:
        saque = int(input('QUANTO VOCÊ QUER SACAR? '))
        tot50 = saque // tot50
        sobra = saque % 50
        
        if sobra // 20 != 0:
            tot20 = sobra // 20
            sobra = sobra % 20
        if sobra // 10 != 0:
                tot10 = sobra // 10
                sobra = sobra % 10
        if sobra // 1 >= 1 or sobra // 1 <= 9:
                    tot1 = sobra // 1
                    sobra = sobra % 1
                    break
        else:
            break

print('='*10)
print(f'''NOTAS DE 50 = {tot50} 
NOTAS DE 20 = {tot20}
NOTAS DE 10 = {tot10}
NOTAS DE 1 = {tot1}''')
print('='*10)

