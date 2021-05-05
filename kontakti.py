#kontakti.py fails satur koda daļu, kura veido datubāzi

from replit import db

#Sākotnējā kontakta pievienošana
def piev_kontaktu(vards, tel_nr):
  if vards in db:
    print("Vārds jau eksistē")
  else:
    db[vards] = tel_nr
    print(f"Pievienots kontakts: {vards} {tel_nr}")
