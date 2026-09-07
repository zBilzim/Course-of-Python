num = int(input('Digite um número: '))
print("""Escolha uma das bases para conversão:
[ 1 ] converter para \033[:32mBINÁRIO\033[m
[ 2 ] Converter para \033[:33mOCTAL\033[m
[ 3 ] Converter para \033[:34mHEXADECIMAL\033[m""")
opçao = int(input('Escolha: '))
if opçao == 1:
    print(f'{num} Convertido para \033[:32mBINÁRIO\033[m é: {bin(num)}')

elif opçao == 2:
    print(f'{num} Convertido para \033[:33mOCTAL\033[m é: {oct(num)}')

elif opçao == 3:
    print(f'{num} Convertido para \033[:34mHEXADECIMAL\033[m é: {hex(num)}')

else:
    print('Escolha apenas entre 1 à 3.')

