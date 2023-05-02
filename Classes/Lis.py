import random

from Classes.Zwierze import Zwierze


class Lis(Zwierze):
    def __init__(self, X, Y, swiat, wiek):
        Zwierze.__init__(self, 'Fox', X, Y, swiat, wiek, 3, 7, False)

    def _losuj_pole(self, cords):
        kierunki = [False, False, False, False]  # 0-góra 1-dół 2-prawo 3-lewo
        if cords[1] < self._swiat.get_wysokosc() - 1 and \
                (self._swiat.get_mapa()[self._X][self._Y + 1] == None or
                 self._swiat.get_mapa()[self._X][self._Y + 1].get_sila() <= self._sila or
                 self._swiat.get_mapa()[self._X][self._Y + 1].get_nazwa() == self._nazwa):
            kierunki[0] = True

        if cords[1] > 0 and \
                (self._swiat.get_mapa()[self._X][self._Y - 1] == None or
                 self._swiat.get_mapa()[self._X][self._Y - 1].get_sila() <= self._sila or
                 self._swiat.get_mapa()[self._X][self._Y - 1].get_nazwa() == self._nazwa):
            kierunki[1] = True

        if cords[0] < self._swiat.get_szerokosc() - 1 and \
                (self._swiat.get_mapa()[self._X + 1][self._Y] == None or
                 self._swiat.get_mapa()[self._X + 1][self._Y].get_sila() <= self._sila or
                 self._swiat.get_mapa()[self._X + 1][self._Y].get_nazwa() == self._nazwa):
            kierunki[2] = True

        if cords[0] > 0 and \
                (self._swiat.get_mapa()[self._X - 1][self._Y] == None or
                 self._swiat.get_mapa()[self._X - 1][self._Y].get_sila() <= self._sila or
                 self._swiat.get_mapa()[self._X - 1][self._Y].get_nazwa() == self._nazwa):
            kierunki[3] = True

        ileKierunkow = 0
        for i in range(0, 4):
            if (kierunki[i]):
                ileKierunkow += 1

        if ileKierunkow > 0:
            kierunek = random.randint(0, ileKierunkow - 1)  # index kierunku (spośród możliwych)
            licznik = -1
            for i in range(0, 4):
                if (kierunki[i]):
                    licznik += 1
                if licznik == kierunek:
                    index = i
                    break

            if index == 0:  # góra
                cords[1] += 1
            elif index == 1:  # dół
                cords[1] -= 1
            elif index == 2:  # prawo
                cords[0] += 1
            elif index == 3:  # lewo
                cords[0] -= 1

    def _rozmnazanie(self, x, y):
        self._swiat.dodaj_info('Foxes reproduce.')
        dziecko = Lis(x, y, self._swiat, 0)
        self._swiat.get_mapa()[x][y] = dziecko
        self._swiat.get_nowo_narodzone().add(dziecko)

    def rysowanie(self):
        return 251, 100, 4
