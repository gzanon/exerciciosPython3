print('====== DESAFIO 029 ======')

vel = float(input('Qual a velocidade do seu carro: '))

if vel <= 80:
    print('Você está dentro do limite, tenha um bom dia.')
else:
    multa = 7 * (vel - 80)
    print('Você está acima da velocidade e foi multado em R$  {:.2f}'.format(multa))