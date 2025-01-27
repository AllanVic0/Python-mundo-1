v = int(input('Qual velocidade você estava? '))
vcalc = (v - 80) * 7


if v > 80:
    print('Você foi multado em R$ {} por ultrapassar o limite de velocidade na pista'.format(vcalc))
else:
    print('Você não foi multado')

