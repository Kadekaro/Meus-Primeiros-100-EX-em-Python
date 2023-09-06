sexo = input('Digite o seu sexo(M para masculino ou F para feminino): ').upper().strip()[0]
while sexo != 'M' and sexo != 'F':
    sexo = input('Comando inválido, por favor digite novamente o seu sexo M ou F: ').upper().strip()[0]
print('O seu sexo é {}!'.format(sexo))
