from Classes.Zwierze import Zwierze


class Wilk(Zwierze):
    def __init__(self, X, Y, swiat, wiek):
        Zwierze.__init__(self, 'Wolf', X, Y, swiat, wiek, 9, 5, False)

    def _rozmnazanie(self, x, y):
        self._swiat.dodaj_info('Wolves reproduce.')
        dziecko = Wilk(x, y, self._swiat, 0)
        self._swiat.get_mapa()[x][y] = dziecko
        self._swiat.get_nowo_narodzone().add(dziecko)

    def rysowanie(self):
        return 80, 80, 80
