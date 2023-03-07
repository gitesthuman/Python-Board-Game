from Classes.Roslina import Roslina


class Mlecz(Roslina):
    def __init__(self, X, Y, swiat, wiek):
        Roslina.__init__(self, 'Mlecz', X, Y, swiat, wiek, 0)

    def akcja(self):
        for i in range(0, 3):
            Roslina.akcja(self)

    def _rozmnazanie(self, x, y):
        self._swiat.dodaj_info('Mlecz rozprzestrzenia się.')
        sadzonka = Mlecz(x, y, self._swiat, 0)
        self._swiat.get_mapa()[x][y] = sadzonka
        self._swiat.get_nowo_narodzone().add(sadzonka)

    def rysowanie(self):
        return (255, 255, 0)