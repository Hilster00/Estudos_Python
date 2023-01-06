import datetime
import locale

#colocar o idioma em português
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

#recebimento da data e conversão para a classe datetime
nascimento=input("Digite sua data de nascimento no formato(dd/mm/aaaa):")
data_nascimento=datetime.datetime.strptime(nascimento,"%d/%m/%Y")

#texo para não precisar digitar a data para cada teste
"""
d='06/01/2001'
data_nascimento=datetime.datetime.strptime(d,"%d/%m/%Y")
"""

#calculo de idade
idade=((datetime.datetime.now()-data_nascimento).days)//365

#separar apenas o dia e mes do aniversario e data atual
aniversario=datetime.datetime.strftime(data_nascimento,"%d/%m")
fez_aniversario=datetime.datetime.strftime(datetime.datetime.now(),"%d/%m")

#calcula a diferenca do dia e mes atual para o dia e mes do aniversario
fez=datetime.datetime.strptime(aniversario,"%d/%m")-datetime.datetime.strptime(fez_aniversario,"%d/%m")

#printa a data atual
today=datetime.datetime.now()
print(f"Hoje é {today.day} de {today.strftime('%B')} de {today.year}")


print(f'Você tem {idade} anos de idade')

#diferenca de data atual para aniversario indica qual caso se encaixa
fez=fez.days
if fez < 0:
    print(f"Você fez aniversário há {abs(fez)} dias, no dia {aniversario}")
elif fez == 0:
    print(f"Parabéns! seu aniversário é hoje, dia {aniversario}")
else:
    print(f"Você fará aniversário em {fez} dias, no dia {aniversario}")

    
