import random

from Classes.Zwierze import Zwierze
from Classes.BarszczSosnowskiego import BarszczSosnowskiego


class CyberOwca(Zwierze):
    def __init__(self, X, Y, swiat, wiek):
        Zwierze.__init__(self, 'Cyber Sheep', X, Y, swiat, wiek, 11, 4, True)

    def akcja(self):
        MAX = self._swiat.get_szerokosc() + self._swiat.get_wysokosc()
        dystans = MAX

        for i in range(0, self._swiat.get_organizmy().get_size()):
            curr = self._swiat.get_organizmy().get_current()
            if isinstance(curr, BarszczSosnowskiego):
                if dystans > abs(self._X - curr.get_X()) + abs(self._Y - curr.get_Y()):
                    dystans = abs(self._X - curr.get_X()) + abs(self._Y - curr.get_Y())
                    cel = curr
            self._swiat.get_organizmy().next()

        for i in range(0, self._swiat.get_nowo_narodzone().get_size()):
            curr = self._swiat.get_nowo_narodzone().get_current()
            if isinstance(curr, BarszczSosnowskiego):
                if dystans > abs(self._X - curr.get_X()) + abs(self._Y - curr.get_Y()):
                    dystans = abs(self._X - curr.get_X()) + abs(self._Y - curr.get_Y())
                    cel = curr
            self._swiat.get_nowo_narodzone().next()

        if dystans < MAX:
            przesuniecie = [0, 0]

            if self._X < cel.get_X():
                przesuniecie[0] = 1
            elif self._X > cel.get_X():
                przesuniecie[0] = -1
            else:
                przesuniecie[0] = 0
            if self._Y < cel.get_Y():
                przesuniecie[1] = 1
            elif self._Y > cel.get_Y():
                przesuniecie[1] = -1
            else:
                przesuniecie[1] = 0

            if przesuniecie[0] != 0 and przesuniecie[1] != 0:
                przesuniecie[random.randint(0, 1)] = 0

            if self._swiat.get_mapa()[self._X + przesuniecie[0]][self._Y + przesuniecie[1]] == None:
                self._ruch(self._X + przesuniecie[0], self._Y + przesuniecie[1])
            else:
                self._swiat.get_mapa()[self._X + przesuniecie[0]][self._Y + przesuniecie[1]].kolizja(self)

        else:
            Zwierze.akcja(self)

    def _rozmnazanie(self, x, y):
        self._swiat.dodaj_info('Cyber Sheep reproduce.')
        dziecko = CyberOwca(x, y, self._swiat, 0)
        self._swiat.get_mapa()[x][y] = dziecko
        self._swiat.get_nowo_narodzone().add(dziecko)

    def rysowanie(self):
        return 0, 0, 0
