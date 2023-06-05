import datetime
import calendar
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

a=datetime.datetime.now()

b=datetime.datetime.strptime('08/08/2001','%d/%m/%Y')
t=datetime.datetime.now()+datetime.timedelta(days=2)
idade=int((a-b).days//365.25)

dias_semana=[t.strftime("%A")]
for i in range(7):
    t=t+datetime.timedelta(days=1)
    dias_semana.append(t.strftime('%A'))
aniversarios_dias={
    i:0 for i in dias_semana
}

while b.year != 2023:
    b=b+datetime.timedelta(days=365.25)
    if (a - b).days < 0:
        break
    aniversarios_dias[b.strftime("%A")]+=1
    


print(a.strftime('%d/%m/%Y'))
print(b.strftime('%d/%m/%Y'))
print(idade)


#print(a.strftime('%A'))
#print(b.strftime('%A'))
#print(calendar.calendar(2023))


for i,j in aniversarios_dias.items():
    print(f'Aniversários no {i}:{j}')
    
    
