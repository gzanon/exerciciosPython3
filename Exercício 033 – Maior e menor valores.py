print('====== DESAFIO 033 ======')

a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))

menor = a
maior = a

if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('O menor valor é {}'.format(menor))
print('O maior valor é {}'.format(maior))