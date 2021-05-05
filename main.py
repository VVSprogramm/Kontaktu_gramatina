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



#Kontaktu rediģēšana
def kontaktu_red():
  iepr_vards = input("Ievadi kontakta vārdu, kuru nepieciešams rediģēt: ")
  iepr_numurs = kontakti.atrod_kont(iepr_vards)

  if iepr_numurs:
    jaunais_vards = input(f"Ievadi kontakta vārdu (atstāj tukšu, ja nevēlies mainīt {iepr_vards})").strip()
    jaunais_numurs = input(f"Ievadi kontakta numuru (atstāj tukšu, ja nevēlies mainīt {iepr_numurs})").strip()
    if not jaunais_numurs:
      jaunais_numurs = iepr_numurs
    if not jaunais_vards:
      kontakti.mainit_numuru(iepr_vards, jaunais_numurs)
    else:
      kontakti.mainit_kontaktu(iepr_vards,jaunais_numurs, jaunais_vards)

  else:
    print(f"Izskatās, ka {iepr_vards} neeksistē")


def kont_dzesana():
  vards = input("Ievadi kontakta vārdu, kuru vēlies dzēst: ")
  kontakts = kontakti.atrod_kont(vards)

  if kontakts:
    print(f'{vards} tika izdzēsts.')
    kontakti.dzest_kontaktu(vards)
  else:
    print(f'Izskatās, ka kontakts {vards} neeksistē')

