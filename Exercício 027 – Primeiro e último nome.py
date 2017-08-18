print('====== DESAFIO 027 ======')

nome = input('Digite seu nome completo: ').strip().lower()

n = nome.split()

print('Muito prazer em te conhecer!')

print('Seu primeiro nome é {}'.format(n[0]))

print('Seu último nome ú {}'.format(n[len(n)-1]))