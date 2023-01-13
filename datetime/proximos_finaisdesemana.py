import datetime
import locale

try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except:
    locale.setlocale(locale.LC_ALL, '')

hoje=datetime.datetime.now()
a=hoje.year+100

while hoje.year < a:
    i=0
    while i < 3:
        if hoje.strftime('%A') in ('sexta','sábado','domingo'):
            if hoje.strftime('%A') == 'domingo':
                print(hoje.strftime('%d/%m/%Y : %A'))
                hoje+=datetime.timedelta(days=1)
                break
            else:
                print(hoje.strftime('%d/%m/%Y : %A'),end=';    ')
            i+=1
        hoje+=datetime.timedelta(days=1)
   
    
    
