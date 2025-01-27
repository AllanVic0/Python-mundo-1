from random import randint

numaleat = randint(0,5)

num = int(input('Escolha um número entre 0 e 5: '))

if num == numaleat:
    print('Parabéns, você acertou!')
else:
    print('Errou')