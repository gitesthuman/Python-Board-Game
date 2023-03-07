from Classes.Roslina import Roslina


class Trawa(Roslina):
    def __init__(self, X, Y, swiat, wiek):
        Roslina.__init__(self, 'Trawa', X, Y, swiat, wiek, 0)

    def _rozmnazanie(self, x, y):
        self._swiat.dodaj_info('Trawa rozprzestrzenia się.')
        sadzonka = Trawa(x, y, self._swiat, 0)
        self._swiat.get_mapa()[x][y] = sadzonka
        self._swiat.get_nowo_narodzone().add(sadzonka)

    def rysowanie(self):
        return (0, 255, 0)
