nome = input('Digite o seu nome completo: ').strip()
print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ', '')))
dividido = nome.split()
print(len(dividido[0]))