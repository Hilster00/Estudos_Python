import datetime
import locale

try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except:
    locale.setlocale(locale.LC_ALL, '')

hoje=datetime.datetime.now()
a=hoje.year+100

while hoje.year < a:
    if hoje.strftime('%A') in ('sexta','sábado','domingo'):
        if hoje.strftime('%A') != 'domingo':
            print(hoje.strftime('%d/%m/%Y : %A'),end=';    ')
        else:
            print(hoje.strftime('%d/%m/%Y : %A'))
    hoje+=datetime.timedelta(days=1)
   
    
