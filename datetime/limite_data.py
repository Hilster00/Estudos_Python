import datetime
import locale

primeira_data=datetime.datetime.strptime(f'01/01/1000',"%d/%m/%Y")
ultima_data=datetime.datetime.strptime(f'31/12/9999',"%d/%m/%Y")

print(f'Primeira data: {datetime.datetime.strftime(primeira_data,"%d/%m/%Y")}')
print(f'Ultima data: {datetime.datetime.strftime(ultima_data,"%d/%m/%Y")}')

try:
    depois_do_fim=ultima_data
    while True:
        depois_do_fim=depois_do_fim+datetime.timedelta(days=1)
        depois_do_fim=datetime.datetime.strftime(depois_do_fim,"%d/%m/%Y")
        depois_do_fim=datetime.datetime.strptime(depois_do_fim,"%d/%m/%Y")
        print(datetime.datetime.strftime(depois_do_fim,"%d/%m/%Y"))
except:
    print(f"Não foi possível ir para depois de {datetime.datetime.strftime(ultima_data,'%d/%m/%Y')}")
 
    
try:
    
    antes_do_inicio=primeira_data
    while True:
        antes_do_inicio=antes_do_inicio-datetime.timedelta(days=1)
        antes_do_inicio=datetime.datetime.strftime(antes_do_inicio,"%d/%m/%Y")
        antes_do_inicio=datetime.datetime.strptime(antes_do_inicio,"%d/%m/%Y")
        print(datetime.datetime.strftime(antes_do_inicio,"%d/%m/%Y"))
    
except:
    print(f"Não foi possível ir para antes de {datetime.datetime.strftime(primeira_data,'%d/%m/%Y')}")
    
