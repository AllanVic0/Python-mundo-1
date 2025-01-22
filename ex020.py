from random import sample

n1 = str(input('Aluno 1: '))
n2 = str(input('Aluno 2: '))
n3 = str(input('Aluno 3: '))
n4 = str(input('Aluno 4: '))

alunos = [n1, n2, n3, n4]

ordem = sample(alunos, k=4)
print('A ordem de apresentação será: {}'.format(ordem))