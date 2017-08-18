print('====== DESAFIO 026 ======')

frase = input('Digite uma frase: ').strip().lower()

print('''A letra A aparece {} vezes na frase.

A primeira letra A aparece na pocição {}

A última letra A aparece na posição {}'''.format(frase.count('a'), frase.find('a')+1, frase.rfind('a')+1))