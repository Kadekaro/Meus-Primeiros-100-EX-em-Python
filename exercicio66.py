n = cont = soma = 0
while n != 999:
    n = int(input('Digite um número (se quiser sair digite 999): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Você digitou {cont} números e a soma entre eles é {soma}!')
