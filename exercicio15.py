km = float(input('\033[34m0Digite quantos km você andou: '))
dias = int(input('Digite por quantos dias você alugou o carro: '))
print("O valor que você irá pagar será de {}R${:.2f}{}\033[34m reais.".format('\033[31m', km * 0.15 + dias * 60, '\033[m'))
