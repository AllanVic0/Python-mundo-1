from math import sqrt

catetoop = float(input('Digite aqui o comprimento do cateto oposto: '))
catetoadj = float(input('Digite aqui o comprimento do cateto adjacente: '))

oposto = catetoop * catetoop
adjacente = catetoadj * catetoadj

somalados = (oposto + adjacente)
hipotenusa = sqrt(somalados)
print('A hipotenusa do seu triângulo retângulo é: {}'.format(hipotenusa))