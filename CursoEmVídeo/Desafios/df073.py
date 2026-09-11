camp = ('','FLAMENGO', 'PALMEIRAS', 'ATHLETICO PARANAENSE', 'FLUMINENSE', 'BAHIA','CRUZEIRO', 'CORITIBA SAF', 'ATLÉTICO MINEIRO', 'RED BULL BRAGANTINO', 'SÃO PAULO', 'EC VITÓRIA', 'CORINTHIANS', 'SANTOS', 'BOTAFOGO', 'GRÊMIO', 'MIRASSOL', 'VASCO DA GAMA', 'INTERNACIONAL', 'REMO', 'CHAPECOENSE')
print('='*20)
print('     5 PRIMEIROS')
print('='*20)
for c in range(1,6):
    print(f'{c} - {camp[c]}')


print('='*20)
print('     4 ÚLTIMOS')
print('='*20)
for c in range(-4,0):
    print(f'{camp[c]}')

print('='*20)
print('  ORDEM ALFABÉTICA')
print('='*20)
for c in range(1,len(camp)):
    print(sorted(camp)[c])


print(f'Chapecoense esta na posição: {camp.index('CHAPECOENSE')}')



