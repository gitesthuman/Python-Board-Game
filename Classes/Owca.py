from Classes.Zwierze import Zwierze


class Owca(Zwierze):
    def __init__(self, X, Y, swiat, wiek):
        Zwierze.__init__(self, 'Sheep', X, Y, swiat, wiek, 4, 4, False)

    def _rozmnazanie(self, x, y):
        self._swiat.dodaj_info('Sheep reproduce.')
        dziecko = Owca(x, y, self._swiat, 0)
        self._swiat.get_mapa()[x][y] = dziecko
        self._swiat.get_nowo_narodzone().add(dziecko)

    def rysowanie(self):
        return 230, 230, 230
