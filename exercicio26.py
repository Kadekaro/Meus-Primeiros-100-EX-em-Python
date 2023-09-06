frase = input('Digite uma frase: ').strip()
print('existem {} letras a na frase.'.format(frase.lower().count('a')))
print('O primeiro a da frase aparece na posição: {}'.format(frase.find('a')+1))
x = frase.replace(' ', '')
print('O ultimo a da frase aparece na posição: {}'.format(x.rfind('a')+1))


# rfind >> começa a procurar a letra do lado direito da frase primeiro (do final para o começo)