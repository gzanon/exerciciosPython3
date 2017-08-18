print('====== DESAFIO 031 ======')

dist = float(input('Qual a distância da sua viagem: '))

if dist <= 200:
    preco = dist * .5
else:
    preco = dist *.45

print('''Você está prestes a começar uma viagem de {:.2f} Km.

Sua viagem custará {:.2f} reais'''.format(dist, preco))