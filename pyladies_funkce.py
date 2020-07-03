import math
def obsah_elipsy(osa_a, osa_b):
  return osa_a * osa_b * math.pi

print(f'Obsah elipsy je {round(obsah_elipsy(20,10),2)} cm2')

# lze napsat i zkracene namisto return vlozit print, ale program tim prichazi o jednu z hlavnich vyhod funkci, pouzit vracenou hodnotu i jinak nez v print, napr. na dalsi vypocet
def obsah_elipsy(osa_a, osa_b):
  print('Obsah je ', round(osa_a * osa_b * math.pi,2), 'cm2')

obsah_elipsy(3,5)

# je dobre funkcim potrebne info predavat jako argumenty a input/print nemit ve funkci ale vne
import math
def obsah_elipsy(osa_a, osa_b):
    # Vrátí obsah elipsy s poloosami daných délek
    # Jen samotný výpočet:
    return osa_a * osa_b * math.pi

# print a input jsou "venku":
x = float(input('Zadej délku poloosy 1: '))
y = float(input('Zadej délku poloosy 2: '))
print('Obsah je', obsah_elipsy(x, y),'cm2')


""" 
# print vypíše nepojmenované argumenty, oddělené mezerou;
# end určuje, co se vypíše na konci (místo přechodu na nový řádek);
# sep udává, co se vypíše mezi jednotlivými argumenty (místo mezery)
print(1, 'dvě', False)
print(1, end=' ')
print(2, 3, 4, sep=', ')

cislo = 5.46
from math import sqrt, floor, ceil
# druhá odmocnina
print(sqrt(cislo))
# zaokrouhlení dolů
print(floor(cislo))
# zaokrouhlení nahoru
print(ceil(cislo)) """