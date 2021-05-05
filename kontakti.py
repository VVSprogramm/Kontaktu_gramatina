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
