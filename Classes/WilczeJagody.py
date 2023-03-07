from Classes.Roslina import Roslina


class WilczeJagody(Roslina):
    def __init__(self, X, Y, swiat, wiek):
        Roslina.__init__(self, 'Wilcze Jagody', X, Y, swiat, wiek, 99)

    def kolizja(self, napastnik):
        Roslina.kolizja(self, napastnik)
        info = 'Wilcze Jagody zatruwają ' + napastnik.get_nazwa() + '!'
        self._swiat.dodaj_info(info)

        if self._swiat.get_organizmy().find_element(self._X, self._Y):
            self._swiat.get_organizmy().del_element(self._X, self._Y)
        else:
            self._swiat.get_nowo_narodzone().del_element(self._X, self._Y)
        self._swiat.get_mapa()[self._X][self._Y] = None

    def _rozmnazanie(self, x, y):
        self._swiat.dodaj_info('Wilcze Jagody rozprzestrzeniają się.')
        sadzonka = WilczeJagody(x, y, self._swiat, 0)
        self._swiat.get_mapa()[x][y] = sadzonka
        self._swiat.get_nowo_narodzone().add(sadzonka)

    def rysowanie(self):
        return (179, 0, 0)