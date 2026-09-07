cid = input('Digite o nome de uma cidade: ')
dividido = cid.split()
#SANTO = dividido[1].upper()
print(f'Essa cidade começa com SANTO? {'SANTO' in dividido[0].upper()}')