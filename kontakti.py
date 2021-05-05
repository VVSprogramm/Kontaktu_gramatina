#kontakti.py fails satur koda daļu, kura veido datubāzi

from replit import db

#Sākotnējā kontakta pievienošana
def piev_kontaktu(vards, tel_nr):
  if vards in db:
    print("Vārds jau eksistē")
  else:
    db[vards] = tel_nr
    print(f"Pievienots kontakts: {vards} {tel_nr}")

#Kontakta atrašana, ievadot pilnu vārdu
def atrod_kont(vards):
  numurs = db.get(vards)
  return numurs

#Kontakta atrašana pēc simboliem
def kont_mekl(meklet):
    sakrit_elementi = db.prefix(meklet)
    return {k: db[k] for k in sakrit_elementi}


#Tiek mainīts tikai kontakta numurs
def mainit_numuru(iepr_vards, jaunais_numurs):
  db[iepr_vards] = jaunais_numurs

def mainit_kontaktu(iepr_vards, jaunais_numurs, jaunais_vards):
  db[jaunais_vards] = jaunais_numurs
  del db[iepr_vards]
