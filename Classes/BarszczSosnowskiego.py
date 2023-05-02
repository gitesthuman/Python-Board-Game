from Classes.Roslina import Roslina
from Classes.Zwierze import Zwierze


class BarszczSosnowskiego(Roslina):
    def __init__(self, X, Y, swiat, wiek):
        Roslina.__init__(self, 'Pine Borscht', X, Y, swiat, wiek, 10)

    def zabij(self, x, y):
        info = f"{self._nazwa} kills {self._swiat.get_mapa()[x][y].get_nazwa()}!"
        self._swiat.dodaj_info(info)

        if self._swiat.get_organizmy().find_element(x, y):
            self._swiat.get_organizmy().del_element(x, y)
        else:
            self._swiat.get_nowo_narodzone().del_element(x, y)
        self._swiat.get_mapa()[x][y] = None

    def akcja(self):
        Roslina.akcja(self)
        if self._Y < self._swiat.get_wysokosc() - 1 and \
                isinstance(self._swiat.get_mapa()[self._X][self._Y + 1], Zwierze) and \
                not self._swiat.get_mapa()[self._X][self._Y + 1].odporny():
            self.zabij(self._X, self._Y + 1)

        if self._Y > 0 and \
                isinstance(self._swiat.get_mapa()[self._X][self._Y - 1], Zwierze) and \
                not self._swiat.get_mapa()[self._X][self._Y - 1].odporny():
            self.zabij(self._X, self._Y - 1)

        if self._X < self._swiat.get_szerokosc() - 1 and \
                isinstance(self._swiat.get_mapa()[self._X + 1][self._Y], Zwierze) and \
                not self._swiat.get_mapa()[self._X + 1][self._Y].odporny():
            self.zabij(self._X + 1, self._Y)

        if self._X > 0 and \
                isinstance(self._swiat.get_mapa()[self._X - 1][self._Y], Zwierze) and \
                not self._swiat.get_mapa()[self._X - 1][self._Y].odporny():
            self.zabij(self._X - 1, self._Y)

    def kolizja(self, napastnik):
        Roslina.kolizja(self, napastnik)
        if self._swiat.get_organizmy().find_element(self._X, self._Y):
            if not self._swiat.get_organizmy().find_element(self._X, self._Y).odporny():
                self._swiat.get_organizmy().del_element(self._X, self._Y)
        else:
            if self._swiat.get_nowo_narodzone().find_element(self._X, self._Y).odporny():
                self._swiat.get_nowo_narodzone().del_element(self._X, self._Y)

        if not self._swiat.get_mapa()[self._X][self._Y].odporny():
            self._swiat.get_mapa()[self._X][self._Y] = None
            info = f"{self._nazwa} poisons {napastnik.get_nazwa()}!"
            self._swiat.dodaj_info(info)

    def rozmnazanie(self, x, y):
        self._swiat.dodaj_info(f'{self._nazwa} spreads.')
        sadzonka = BarszczSosnowskiego(x, y, self._swiat, 0)
        self._swiat.get_mapa()[x][y] = sadzonka
        self._swiat.get_nowo_narodzone().add(sadzonka)

    def rysowanie(self):
        return 255, 0, 0
