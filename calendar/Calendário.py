import calendar
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
calendar.setfirstweekday(calendar.SUNDAY)

ano=int(input("Informe um ano:"))
print(f'Calendário de {ano}')
print(calendar.calendar(ano))
