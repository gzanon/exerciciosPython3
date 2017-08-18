print('====== DESAFIO 035 ======')

print('Verifique se os valores formam um triângulo.')

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os seguimentos acima podem formar um triângulo.')
else:
    print('Os segmentos acima não podem formar um triângulo.')