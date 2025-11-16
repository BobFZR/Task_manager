def hlavni_menu():
  print()
  print("Správce úkolů - Hlavní menu")
  print("1. Přidat nový úkol")
  print("2. Zobrazit všechny úkoly")
  print("3. Odstranit úkol")
  print("4. Konec programu")
  volba = input("Vyberte možnost(1-4): ")
  print()
  return volba

def pridat_ukol():
  while True:
    nazev = input("Zadejte název úkolu: ")
    popis = input("Zadejte popis úkolu: ")
    if not nazev or not popis:
      print("Název a popis úkolu nemohou být prázdné.\n")
    else:
      break
  ukol = {"Název": nazev, "Popis": popis}
  return ukol

def zobrazit_ukoly(ukoly):
  print("Seznam úkolů:")
  if not ukoly:
    print("Žádné úkoly k zobrazení.\n")
    return
  for index, ukol in enumerate(ukoly, start=1):
    print(f"{index}.{ukol['Název']} - {ukol['Popis']}")


def odstranit_ukol(ukoly):
  if not ukoly:
    print("Nejsou žádné úkoly k odstranění.\n")
    return

  zobrazit_ukoly(ukoly)
  while True:
    try:
      cislo_ukolu = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
      if 1 <= cislo_ukolu <= len(ukoly):
        break
      else:
        print(f"Neplatné číslo úkolu. Zadejte číslo mezi 1 a {len(ukoly)}.")
    except ValueError:
      print("Neplatný vstup. Zadejte prosím číslo.\n")

  nazev= ukoly[cislo_ukolu - 1]["Název"]
  ukoly.pop(cislo_ukolu - 1)
  print(f"Úkol '{nazev}' byl odstraněn.")


ukoly = []
volba = hlavni_menu()
while volba != "4":
  if volba == "1":
    ukol = pridat_ukol()
    ukoly.append(ukol)
  elif volba == "2":
    zobrazit_ukoly(ukoly)
  elif volba == "3":
    odstranit_ukol(ukoly)
  else:
    print("Neplatná volba. Zadejte číslo 1-4.")
  volba = hlavni_menu()
else:
  print("Konec programu.")