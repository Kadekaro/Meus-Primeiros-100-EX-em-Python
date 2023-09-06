ano = int(input('Digite o ano de nascimento no formato aaaa: '))
if 2018 - ano == 18:
    print('\033[31mVocê tem que se alistar esse ano no serviço militar!')
elif 2018 - ano > 18:
    print('\033[34mA sua idade passou do tempo certo para o alistamento no serviço militar,'
          ' verifique isso o quanto antes'
          ' no orgão responsável em seu município! Você passou {}{}{} \033[34mano(s) do'
          ' tempo de alistamento!'.format('\033[31m', 2018 - ano - 18, '\033[m'))
else:
    print('\033[31mAinda falta {} ano(s) para você se alistar no serviço militar,'
          ' no ano em que completar 18 anos vá até a junta de serviço militar de seu município'
          ' e se aliste neste mesmo ano!'.format(2018 - ano - 18).replace('-', ''))
