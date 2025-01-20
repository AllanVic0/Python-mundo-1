base = int(input('Digite quantos metros mede a base da sua parede: '))
altura = int(input('Digite quantos metros de altura tem a sua parede: '))

area = base * altura
tinta = area / 2
print('Sua parede tem {}m²'.format(area))
print('Você vai precisar de {}L de tinta'.format(tinta))