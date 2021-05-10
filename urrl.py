#agarrar ip de una url

import socket
from ip2geotools.databases.noncommercial import DbIpCity

url = input("metele un url:")
IP = socket.gethostbyname(url)
response = DbIpCity.get(IP, api_key='free')
print("IP:", IP)
print("City:", response.city)
print("Region:", response.region)
print("Country:", response.country)