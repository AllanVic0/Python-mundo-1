import math

# Caso importe somente o módulo de sqrt, pode ser feito dessa maneira. Também é possível importar mais de um módulo ao mesmo tempo.
# from math import sqrt, floor
# raiz = sqrt(num)

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.trunc(raiz)))

# math.ceil - arredonda o numero para cima (ex: 5.67 vira 6)
# math.floor - arredonda o numero para baixo (ex: 5.45 vira 5)
# math.trunc - Remove as casas decimais do número, deixando ele truncado
# math.pow - Tem a mesma função de **
# math.sqrt - Tem a função de trazer a raiz quadrada do número
# math.factorial - Faz a fatorial do número