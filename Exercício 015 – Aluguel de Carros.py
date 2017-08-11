print('====== DESAFIO 015 ======')
dias = int(input('Quantos dias alugados: '))
km = float(input('Quantos Km rodados: '))
custo = 60*dias + .15*km
print('O total a pagar é de R$ {}'.format(custo))