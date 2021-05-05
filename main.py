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


#Kontaktu atrašana gan pēc pilna vārda, gan pēc simboliem
def kont_atrasana():
  vards = input("Ivadi kontakta vārdu, kuru meklē: ")
  numurs = kontakti.atrod_kont(vards)

  if numurs:
    print(f"{vards} numurs ir {numurs}")
  else:
    sakrit = kontakti.kont_mekl(vards)
    if sakrit:
      for k in sakrit:
        print(f"{k} numurs ir {sakrit[k]}")
    else:
      print(f"Izskatās, ka {vards} nav sarakstā")
