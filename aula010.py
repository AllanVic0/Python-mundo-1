
# Sintaxe if else
# tempo = int(input('Quantos anos tem o seu carro? '))

# if tempo <= 3:
#     print('O seu carro é novo.')

# else:
#     print('O seu carro é velho.')


# Exemplo:
n1 = float(input('Digite a sua nota da 1º unidade: '))
n2 = float(input('Digite a sua nota da 2º unidade: '))
media = (n1 + n2) / 2
print('A sua média é: {:.1f}'.format(media))

if media >= 6:
    print('Aprovado')
else:
    print('Recuperação')
print('---Fim---')