import requests
import os
os.system('figlet TAYRELW')
print("""
	===========================
	[1] CONSULTA CEP.       
	===========================
	""")
a = int(input('DIGITE O CEP: '))
b = requests.get('https://viacep.com.br/ws/{}/xml/'.format(a))
print (b.text)
