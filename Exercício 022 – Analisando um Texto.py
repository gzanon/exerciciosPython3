print('====== DESAFIO 022 ======')

nome = input('Digite seu nome completo: ')

print('''Analisando seu nome ...
Seu nome em maiúsculas é {}
Seu nome em minúsculas é {}
Seu nome tem ao todo {} letras
Seu primeiro nome é {} e tem {} letras'''.format(nome.upper(), nome.lower(), len(nome)-nome.count(' '), nome.split()[0], len(nome.split()[0])))
