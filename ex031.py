km = float(input('Quantos km tem a viagem? '))

if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45
print('Sua passagem custa R$ {:.2f}'.format(preco))