from random import randint
from time import sleep

print('====== DESAFIO 028 ======')

print('=-='*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)

num = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')

n = randint(0, 5)
sleep(3)

if num == n:
    print('Parabéns, você acertou!')
else:
    print('Você errou, eu pensei no número {}'.format(n))