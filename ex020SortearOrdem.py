import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1,a2,a3,a4]
#random.shuffle(lista)
#print('A sequência de apresentação de trabalhos será: {}'.format(lista))

embaralha = random.sample(lista,3)
print('A sequência de apresentação de trabalhos será: {}'.format(embaralha)) #outra maneira que deu certo foi usando o sample, nele eu consigo dizer quantas eu quero que sejam sorteadas, o shuffle apenas embaralha

