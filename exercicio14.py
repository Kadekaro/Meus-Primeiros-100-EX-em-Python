c = float(input('\033[34mDitite uma temperatura em °c: '))
f = ((9*c)/5)+32 # <<< fórmula da temperatura de celsos para fahrenheit
print('O valor em fahrenheit será {}°{:.2f}{}\033[34m de {}°{:.2f}{}\033[34m celsos \033[m'.format('\033[31m', f, '\033[m', '\033[31m', c, '\033[m'))

