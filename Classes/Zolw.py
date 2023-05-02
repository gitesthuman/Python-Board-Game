import random

from Classes.Zwierze import Zwierze


class Zolw(Zwierze):
    def __init__(self, X, Y, swiat, wiek):
        Zwierze.__init__(self, 'Tortoise', X, Y, swiat, wiek, 2, 1, False)

    def akcja(self):
        if random.randint(1, 4) == 1:
            Zwierze.akcja(self)

    def kolizja(self, napastnik):
        if self._nazwa != napastnik.get_nazwa() and napastnik.get_sila() < 5:  # obrona
            info = f"{napastnik.get_nazwa()} attacks {self._nazwa}! {self._nazwa} defends himself!"
            self._swiat.dodaj_info(info)
        else:
            Zwierze.kolizja(self, napastnik)

    def _rozmnazanie(self, x, y):
        self._swiat.dodaj_info('Tortoises reproduce.')
        dziecko = Zolw(x, y, self._swiat, 0)
        self._swiat.get_mapa()[x][y] = dziecko
        self._swiat.get_nowo_narodzone().add(dziecko)

    def rysowanie(self):
        return 153, 89, 0