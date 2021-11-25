n = float(input('Digite o valor da roupa: '))
desconto = n*0.05
valor = n-desconto
print('O desconto da roupa foi de R${:.2f}, logo você comprará ela por apenas R${:.2f}'.format(desconto,valor))