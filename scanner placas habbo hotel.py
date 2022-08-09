import requests
import os
from colorama import Back, Fore, init

init()


print(Fore.BLUE)
HabboNombre = input("Escribe el nombre del keko: ") 
print("Elige el hotel: es/com/fi/com.br/fr/nl/de/it/com.tr")
Hotel = input("hotel: ")
response = requests.get(f'https://www.habbo.{Hotel}/api/public/users?name={HabboNombre}')








HabboNombre = response.json()['uniqueId']
print(HabboNombre)
os.system("cls")
    
url= f'https://www.habbo.{Hotel}/api/public/users/{HabboNombre}/badges'



r= requests.get(url)
habbo = r.text

habbo = r.json()


for Habboinfo in habbo:
    
    
    print(Fore.RED + "Nombre Placa: " + Fore.YELLOW + Habboinfo["name"])
    print("\n")
    print(Fore.CYAN + "Descripción Placa: " + Fore.MAGENTA + Habboinfo["description"])
    print("\n")
    print(Fore.GREEN + "Código Placa: " + Fore.RED + Habboinfo["code"])
    
    
    
    
    print(Fore.WHITE + "*****************************************")
    
print("                                                                                                   Creado Por Jose89fcb")

print("\n\n\n")
length = len(habbo)

print(Fore.CYAN + "Total placas:",  length) 

print(Fore.YELLOW)
os.system("pause")
