import kontakti #tiek importēts fails "kontakti.py"
from os import system
sakums = """ Sveicināti!
------------------------------
Lūdzu, izvēlieties darbību:
1 - pievienot jaunu kontaktu
2 - atrast kontaktu
3 - rediģēt kontaktu
4 - kontaktu dzēšana
------------------------------
"""

#Kontaktu pievienošana
def kontaktu_piev():
 vards = input("Lūdzu, ievadiet kontakta vārdu: ")
 numurs = input("Lūdzu, ievadiet kontakta numuru: ")

 kontakti.piev_kontaktu(vards, numurs)
