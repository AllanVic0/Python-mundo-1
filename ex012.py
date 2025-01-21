preco = float(input('Insira aqui o preço do produto desejado: '))
desc =  5 * preco / 100
novopreco = preco - desc
print ('O valor total com desconto de 5% é {:.2f}'.format(novopreco))