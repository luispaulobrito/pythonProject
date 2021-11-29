d = int(input('Quantos dias alugados: '))
k = float(input('Quantos kilômetros rodados: '))
total = (d*60)+(k*0.15)
print('O total a pagar é: {:.2f}'.format(total))