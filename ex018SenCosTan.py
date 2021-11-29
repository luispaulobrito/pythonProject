import math
num = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(num))
coseno = math.cos(math.radians(num))
tangente = math.tan(math.radians(num))
print('Seno: {:.2f}'.format(seno))
print('Coseno: {:.2f}'.format(coseno))
print('Tangente: {:.2f}'.format(tangente))