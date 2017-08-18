from datetime import date



print('====== DESAFIO 032 ======')

ano = int(input('Que ano que analisar? Coloque 0 para o ano atual: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))