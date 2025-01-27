ano = int(input('Digite o ano: '))

calc = ano % 4
calc2 = ano % 400

if calc == 0 and calc2 == 0:
    print('É bissexto')
else:
    print('Não é bissexto')


# versão mais simples
# if ano % 4 == 0:
#     print('Bissexto')
# else:
#     print('Não é bissexto')