from calendar import weekday
from datetime import *
semana = date.today().weekday()
if semana == 0:
    semana = 'segunda-feira'
if semana == 1:
    semana = 'terça-feira'
if semana == 2:
    semana = 'quarta-feira'
if semana == 3:
    semana = 'quinta-feira'
if semana == 4:
    semana = 'sexta-feira'
if semana == 5:
    semana = 'sabado'
if semana == 6:
    semana = 'domingo'
Data_hora = datetime.now()
dataEhora = Data_hora.strftime('%d/%m/%Y %H:%M')
print(semana,dataEhora)
