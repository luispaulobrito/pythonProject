import math
co = float(input('Qual o valor do cateto oposto? '))
ca = float(input('Qual o valor do cateto adjacente? '))
print('O valor da hipotenusa é igaul a: {:.2f}'.format(math.hypot(co,ca)))
