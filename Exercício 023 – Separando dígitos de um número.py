print('====== DESAFIO 023 ======')

num = int(input('Informe um número: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('''Analisando o número {}
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}'''.format(num, u, d, c, m))