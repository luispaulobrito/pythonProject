real = float(input('Digite o valor em reais para converter: '))
dolar = real/5.61
euro = real/6.33
pesoarg = real*18.00
pesouru = real*7.89
print('Esse valor em dólar é: U${:.2f}'.format(dolar))
print('Esse valor em euro é: €{:.2f}'.format(euro))
print('Esse valor em peso argentino é: ${:.2f}'.format(pesoarg))
print('Esse valor em peso uruguaio é: ${:.2f}'.format(pesouru))

