import datetime 

def printar_mes(mes,ano):
    #ajustando data 
    data = datetime.datetime.strptime(f"{mes}/{ano}","%m/%Y")
    
    #ultimo dia do mês
    final = data.replace(day = 1, month=data.month%12+1, year=data.year+(data.month//12))- datetime.timedelta(days=1)
    final = final.day
    
    #print do calendário
    print(data.strftime("%B/%Y"))
    print("dom|seg|ter|qua|qui|sex|sab")
    
    #semana
    semana = ""
    if data.weekday() != 6:
        semana += "   |"*(data.weekday()+1)
    
    for i in range(final):
        semana+=f" {data.strftime('%d')}"
        data+=datetime.timedelta(days=1)
        if data.weekday() == 6:
            print(semana)
            semana=""
        else:
            semana+="|"
    print(semana)
    
def printar_ano(ano):
    print(f"ANO: {datetime.datetime.strptime(str(ano),'%Y').strftime('%y')}")
    for i in range(1,13):
        printar_mes(i,ano)
        
        
#printar_mes('8','2001')   
#printar_mes('8','2001') 
printar_ano('2024')


hoje = datetime.datetime.now()
data = datetime.datetime.strptime("08/08/2001", "%d/%m/%Y")
data2 = data.strftime("%m")
str_data = data.strftime("%d/%Y/")
str_data += str(int(data2)+1)
data2 = datetime.datetime.strptime(str_data,"%d/%Y/%m")
print(hoje.strftime("%d"))
print(data.strftime("%d/%m/%Y"))
print(data2)


print("Hello World")
