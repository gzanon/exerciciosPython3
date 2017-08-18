print('====== DESAFIO 034 ======')

salario = float(input('Informe o seu salário: '))

if salario > 1250:
    aumento = salario * 1.1
else:
    aumento = salario * 1.15
print('Seu novo salário será R${}'.format(aumento))