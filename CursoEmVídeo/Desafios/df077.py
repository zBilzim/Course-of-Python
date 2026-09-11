tupla = ('KYNBUNDAO',
         'CELULAR',
         'CUZINDOKYN',
         'CALÇA',
         'CANSEI',
         'DAMEUNGRR',
         'UNQUE',
         'UNGRR'
)

for c in tupla:
    print(f'\nNa palavra {c} temos: ', end=' ')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')