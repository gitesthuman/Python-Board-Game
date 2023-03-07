import random

from Classes.Zwierze import Zwierze


class Zolw(Zwierze):
    def __init__(self, X, Y, swiat, wiek):
        Zwierze.__init__(self, 'Żółw', X, Y, swiat, wiek, 2, 1, False)

    def akcja(self):
        if random.randint(1, 4) == 1:
            Zwierze.akcja(self)

    def kolizja(self, napastnik):
        if self._nazwa != napastnik.get_nazwa() and napastnik.get_sila() < 5: # obrona
            info = napastnik.get_nazwa() + ' atakuje Żółw! Żółw broni się!'
            self._swiat.dodaj_info(info)
        else:
            Zwierze.kolizja(self, napastnik)

    def _rozmnazanie(self, x, y):
        self._swiat.dodaj_info('Żółwie rozmnażają się.')
        dziecko = Zolw(x, y, self._swiat, 0)
        self._swiat.get_mapa()[x][y] = dziecko
        self._swiat.get_nowo_narodzone().add(dziecko)

    def rysowanie(self):
        return (153, 89, 0)