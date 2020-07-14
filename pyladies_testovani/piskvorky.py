import random

def tah(pole, cislo_policka, symbol):
    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]

def tah_hrace(pole):
    while True:
        cislo_policka = input("Zadej cislo policka 0-19: ")
        cislo_policka = int(cislo_policka)
        if cislo_policka < 0 or cislo_policka > 19:
            print("Zadej cislo v rozmezi 0-19.")
        elif pole[cislo_policka] != "-":
            print(f"Policko {cislo_policka} je obsazene, vyber jine.")
        else:
            return tah(pole, cislo_policka, "x")

def tah_pocitace(pole):
    while True:
        cislo_policka = random.randrange(len(pole))
        if pole[cislo_policka] == "-":
            return tah(pole, cislo_policka, "o")

def vyhodnot(pole):
    if "xxx" in pole:
        return "x"
    elif "ooo" in pole:
        return "o"
    elif "-" not in pole:
        return "!"
    else:
        return "-"

def piskvorky1d():
  na_tahu = "x"
  pole = "-" * 20
  while True:
      if na_tahu == "x":
          pole = tah_hrace(pole)
          na_tahu = "o"
      elif na_tahu == "o":
          pole = tah_pocitace(pole)
          na_tahu = "x"

      vysledek = vyhodnot(pole)
      print(pole)

      if vysledek != "-":
          if vysledek == "!":
              print(f"Remiza! {pole}")
          elif vysledek == "x":
              print(f"Vyhravas nad pocitacem! {pole}")
          elif vysledek == "o":
              print(f"Bohuzel, pocitac vyhral. {pole}")
          else:
              raise ValueError(f"Nepripustny vysledek hry '{vysledek}'")
          break