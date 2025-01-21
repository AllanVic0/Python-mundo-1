km = float(input('Quantos km foram percorridos com o veículo? '))
dias = float(input('Quantos dias o carro ficou alugado? '))

percorrido = (km * 0.15)
diasutil = (dias * 60)
total = (percorrido + diasutil)

print('\n O valor total do aluguel do seu carro foi: R$ {}\n \n Quilômetros percorridos: R$ {:.2f}\n Dias utilizados: R$ {:.2f}'.format(total, percorrido, diasutil))