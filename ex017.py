import math

catetoop = float(input('Digite aqui o comprimento do cateto oposto: '))
catetoadj = float(input('Digite aqui o comprimento do cateto adjacente: '))

# hipotenusa = math.hypot(catetoop, catetoadj) só essa linha basta para resolver esse desafio

oposto = catetoop * catetoop
adjacente = catetoadj * catetoadj

somalados = (oposto + adjacente)
hipotenusa = math.sqrt(somalados)
print('A hipotenusa do seu triângulo retângulo é: {:.2f}'.format(hipotenusa))