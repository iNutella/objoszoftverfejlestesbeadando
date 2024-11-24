from abc import ABC, abstractmethod
from datetime import datetime
import re

# Abstract Auto class
class Auto(ABC):
    def __init__(self, rendszam, tipus, berleti_dij):
        if re.fullmatch("([A-Z]){3,4}\-(\d){3}",rendszam) is not None: #Ez a sor azt ellenőrzi, hogy megfelelő formátumban van megadva a rendszám, hogy ne lehessen hamis rendszámot hozzáadni
            self.rendszam = rendszam
        self.tipus = tipus
        self.berleti_dij = berleti_dij

    @abstractmethod
    def __str__(self):
        pass

# Személyauto class
class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, utas_kapacitas):
        super().__init__(rendszam, tipus, berleti_dij)
        self.utas_kapacitas = utas_kapacitas

    def __str__(self):
        return f"Személyautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Bérleti díj: {self.berleti_dij}, Utas kapacitás: {self.utas_kapacitas}"

# Teherauto class
class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, teher_kapacitas):
        super().__init__(rendszam, tipus, berleti_dij)
        self.teher_kapacitas = teher_kapacitas

    def __str__(self):
        return f"Teherautó - Rendszám: {self.rendszam}, Típus: {self.tipus}, Bérleti díj: {self.berleti_dij}, Teher kapacitás: {self.teher_kapacitas} kg"

# Berles class
class Berles:
    def __init__(self, auto, datum):
        self.auto = auto
        self.datum = datum

    def __str__(self):
        return f"Bérlés - Autó: {self.auto.rendszam}, Dátum: {self.datum}"

# Autokolcsonzo class
class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []
        self.autok_hozzaadasa(Szemelyauto("LOL-123", "Skoda VRS Octavia", 10000, 5))
        self.autok_hozzaadasa(Szemelyauto("FAD-340", "Toyota Supra", 12000, 5))
        self.autok_hozzaadasa(Teherauto("TOMI-001", "Ford Raptor", 15000, 1000))
        self.auto_berlese("LOL-123", "2024-11-25",True)
        self.auto_berlese("FAD-340", "2024-12-26",True)
        self.auto_berlese("TOMI-001", "2025-11-27",True)
        self.auto_berlese("LOL-123", "2024-10-28",True)

    def autok_hozzaadasa(self, auto):
        self.autok.append(auto)

    def auto_berlese(self, rendszam, datum,kezdo):
        for auto in self.autok:
            if auto.rendszam == rendszam:
                if not any(berles.auto == auto and berles.datum == datum for berles in self.berlesek):
                    self.berlesek.append(Berles(auto, datum))
                    if kezdo is False:
                        print(f"Sikeresen bérelted az autót: {auto.rendszam}")
                    return auto.berleti_dij
                else:
                    print("Az autó már foglalt a megadott napon.")
                    return None
        print("Nem található ilyen rendszámú autó.")
        return None

    def berles_lemondasa(self, rendszam, datum):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam and berles.datum == datum:
                self.berlesek.remove(berles)
                print("Sikeresen lemondtad a bérlést.")
                return True
        print("Nem található ilyen bérlés.")
        return False

    def berlesek_listazasa(self):
        if self.berlesek:
            for berles in self.berlesek:
                print(berles)
        else:
            print("Nincs aktív bérlés.")

# Program inicializálása
def main():
    kolcsonzo = Autokolcsonzo("RenTomi's cars")

    # Felhasználói interfész
    while True:
        print("Autókölcsönző Rendszer")
        print("Cégneve: "+kolcsonzo.nev)
        print("1. Autó bérlése")
        print("2. Bérlés lemondása")
        print("3. Bérlések listázása")
        print("4. Kilépés")
        valasztas = input("Válassz egy lehetőséget: ")

        if valasztas == "1":
            rendszam = input("Add meg az autó rendszámát: ")
            datum = input("Add meg a bérlés dátumát (YYYY-MM-DD): ")
            try:
                datetime.strptime(datum, "%Y-%m-%d")
                kolcsonzo.auto_berlese(rendszam, datum)
            except ValueError:
                print("Érvénytelen dátumformátum.")
        elif valasztas == "2":
            rendszam = input("Add meg az autó rendszámát: ")
            datum = input("Add meg a bérlés dátumát (YYYY-MM-DD): ")
            kolcsonzo.berles_lemondasa(rendszam, datum)
        elif valasztas == "3":
            kolcsonzo.berlesek_listazasa()
        elif valasztas == "4":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    main()