from datetime import *
data = date.today()
dataMes = '{}/{}/{}'.format( data.day, data.month,data.year)
print(dataMes)
if data.month == 1:
    print('janeiro')
if data.month == 2:
    print('fevereiro')
if data.month == 3:
    print('março')
if data.month == 4:
    print('abril')
if data.month == 5:
    print('maio')
if data.month == 6:
    print('junho')
if data.month == 7:
    print('julho')
if data.month == 8:
    print('agosto')
if data.month == 9:
    print('setembro')
if data.month == 10:
    print('outubro')
if data.month == 11:
    print('novembro')
if data.month == 12:
    print('dezembro')

