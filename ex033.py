print('Digite três números abaixo: ')
num1 = int(input('Primeiro valor:  '))
num2 = int(input('Segundo valor:  '))
num3 = int(input('Terceiro valor:  '))

if num1 > num2 and num1 > num3:
    print('{} é o maior numero'.format(num1))
elif num2 > num1 and num2 > num3:
    print('{} é o maior numero'.format(num2))
else:
    print('{} é o maior numero'.format(num3))
