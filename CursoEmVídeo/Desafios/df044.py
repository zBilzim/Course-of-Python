valor = 2200.99
print(f'TV TCL por R$ {valor}')
s = input('Você quer comprar? ')
if s in 'S Sim s sim':
    print('Certo, você tem 4 opções de compra: ')
    print('1 - À vista dinheiro/cheque: 10% de desconto')
    cheq = valor - (valor*0.1)
    print(f'Ficando: {cheq:.2f}')

    print('2 - À vista no cartão: 5% de desconto')
    cart = valor - (valor*0.05)
    print(f'Ficando: {cart:.2f}')

    print('3 - Em até 2x no cartão: preço normal.')
    print(valor/2)

    print('4 - Em até 3x ou mais no cartão: 20% de juros')
    juros = (valor*1.2) / 3
    print(f'Caso em 3x, fica: {juros:.2f}')

    resp = int(input('Qual você quer?[1,2,3,4] '))
    if resp == 1:
        print(f'Ótima escolha. Você pagará um cheque de R${cheq:.2f} ')

    elif resp == 2:
        print(f'Ótima escolha. Você pagará no débito R${cart:.2F} ')

    elif resp == 3:
        print(f'Ótima escolha, você irá parcelar o valor original em duas vezes.\nFicando: R${valor/2:.2f} 2x')

    elif resp == 4:
        parc = float(input('Boa escolha, você ira pagar em quantas vezes? '))
        val = (valor*1.2) / parc
        print(f'As parcelas vão ficar: R${val:.2f} em {parc}x')




else:
    print('Ótimo então.')