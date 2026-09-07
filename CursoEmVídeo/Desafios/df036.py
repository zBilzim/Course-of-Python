print('===Aprovação de Empréstimo===')
casa = float(input('Digite o valor da casa: '))
sal = float(input('Digite o valor do seu salário: '))
temp = int(input('Em quantos anos você vai pagar? '))
aux = (temp * 12)
exc = (sal*1.3) - sal
if casa/aux < exc:
    emp = casa/aux
    print(f'Seus empréstimos serão de R${emp:.2f} em {temp} anos.')

else:
    print('Empréstimo NEGADO')


