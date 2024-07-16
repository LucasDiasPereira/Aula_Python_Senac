import http.client
import json
from datetime import datetime
import calendar
 
ano = input ('Qual ano deseja consultar: ')
site = http.client.HTTPSConnection("brasilapi.com.br")
 
site.request ("GET", f"/api/feriados/v1/{ano}")
response = site.getresponse()
res = response.read()
 
 
feriados = json.loads(res.decode('utf-8'))
 
for feriado in feriados:
    print (f"Data: {feriado['date']}")
    str_data = feriado['date']
    print (str_data)
    date = datetime.strptime(str_data, '%Y-%m-%d').date()
    print (f"Dia da semana: {calendar.day_name[date.weekday()]}")
    print (f"Nome: {feriado['name']}")
    print (f"Data: {feriado['type']}\n")
