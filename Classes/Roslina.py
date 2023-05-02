import random

from Classes.Organizm import Organizm


class Roslina(Organizm):
    def __init__(self, nazwa, X, Y, swiat, wiek, sila):
        Organizm.__init__(self, nazwa, X, Y, swiat, wiek, sila, 0)

    def _losujPole(self, cords):
        kierunki = [False, False, False, False] # 0-góra 1-dół 2-prawo 3-lewo
        if cords[1] < self._swiat.get_wysokosc() - 1 and self._swiat.get_mapa()[self._X][self._Y + 1] == None:
            kierunki[0] = True
        if cords[1] > 0 and self._swiat.get_mapa()[self._X][self._Y - 1] == None:
            kierunki[1] = True
        if cords[0] < self._swiat.get_szerokosc() - 1  and self._swiat.get_mapa()[self._X + 1][self._Y] == None:
            kierunki[2] = True
        if cords[1] > 0  and self._swiat.get_mapa()[self._X - 1][self._Y] == None:
            kierunki[3] = True

        ileKierunkow = 0
        for i in range(0, 4):
            if (kierunki[i]):
                ileKierunkow += 1

        if ileKierunkow > 0:
            kierunek = random.randint(0, ileKierunkow - 1) # index kierunku (spośród możliwych)
            licznik = -1
            for i in range(0, 4):
                if (kierunki[i]):
                    licznik += 1
                if licznik == kierunek:
                    index = i
                    break

            if index == 0: #góra
                cords[1] += 1
            elif index == 1: #dół
                cords[1] -= 1
            elif index == 2: #prawo
                cords[0] += 1
            elif index == 3: #lewo
                cords[0] -= 1

    def akcja(self):
        if random.randint(1, 20) == 1:
            cords = [self._X, self._Y]
            self._losujPole(cords)
            if cords[0] != self._X or cords[1] != self._Y:
                self._rozmnazanie(cords[0], cords[1])

    def kolizja(self, napastnik):
        info = napastnik.get_nazwa() + ' eats ' + self._nazwa + '!'
        self._swiat.dodaj_info(info)

        if self._swiat.get_organizmy().find_element(self._X, self._Y) != None:
            self._swiat.get_organizmy().del_element(self._X, self._Y)
        else:
            self._swiat.get_nowo_narodzone().del_element(self._X, self._Y)
        self._swiat.get_mapa()[self._X][self._Y] = napastnik
        self._swiat.get_mapa()[napastnik.get_X()][napastnik.get_Y()] = None
        self._swiat.get_organizmy().find_element(napastnik.get_X(), napastnik.get_Y()).set_X(self._X)
        self._swiat.get_organizmy().find_element(self._X, napastnik.get_Y()).set_Y(self._Y)
        self._swiat.get_mapa()[self._X][self._Y].set_X(self._X)
        self._swiat.get_mapa()[self._X][self._Y].set_Y(self._Y)