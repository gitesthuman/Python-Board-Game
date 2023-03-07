import random

from Classes.Zwierze import Zwierze


class Antylopa(Zwierze):
    def __init__(self, X, Y, swiat, wiek):
        Zwierze.__init__(self, 'Antylopa', X, Y, swiat, wiek, 4, 4, False)

    def kolizja(self, napastnik):
        if self._nazwa != napastnik.get_nazwa() and random.randint(1, 2) == 1: # unik
            kierunki = [False,False,False,False] # 0-góra 1-dół 2-prawo 3-lewo

            if self._Y < self._swiat.get_wysokosc() - 1 and self._swiat.get_mapa()[self._X][self._Y + 1] == None:
                kierunki[0] = True
            if self._Y > 0 and self._swiat.get_mapa()[self._X][self._Y - 1] == None:
                kierunki[1] = True
            if self._X < self._swiat.get_szerokosc() - 1 and self._swiat.get_mapa()[self._X + 1][self._Y] == None:
                kierunki[2] = True
            if self._X > 0 and self._swiat.get_mapa()[self._X - 1][self._Y] == None:
                kierunki[3] = True

            ileKierunkow = 0
            for i in range(0, 4):
                if kierunki[i]:
                    ileKierunkow += 1

            if ileKierunkow > 0: # unik udany
                info = str(napastnik.get_nazwa()) + ' atakuje Antylopa! Antylopa robi unik!'
                self._swiat.dodaj_info(info)
                kierunek = random.randint(0, ileKierunkow - 1) # index kierunku (spośród możliwych)
                licznik = -1
                for i in range(0, 4):
                    if (kierunki[i]):
                        licznik += 1
                    if licznik == kierunek:
                        index = i
                        break

                x = self._X
                y = self._Y

                if index == 0: # góra
                    self._ruch(self._X, self._Y + 1)
                elif index == 1: # dół
                    self._ruch(self._X, self._Y - 1)
                elif index == 2: # prawo
                    self._ruch(self._X + 1, self._Y)
                elif index == 3: # lewo
                    self._ruch(self._X - 1, self._Y)

                self._swiat.get_mapa()[napastnik.get_X()][napastnik.get_Y()] = None
                self._swiat.get_organizmy().find_element(napastnik.get_X(), napastnik.get_Y()).set_X(x)
                self._swiat.get_organizmy().find_element(x, napastnik.get_Y()).set_Y(y)
                napastnik.set_X(x)
                napastnik.set_Y(y)
                self._swiat.get_mapa()[napastnik.get_X()][napastnik.get_Y()] = napastnik
                return

        # unik nieudany, więc walka
        Zwierze.kolizja(self, napastnik)

    def _losuj_pole(self, cords):
        kierunki = [False, False, False, False, False, False, False, False] #0-góra 1-dół 2-prawo 3-lewo 4-góra2 5-dół2 6-prawo2 7-lewo2

        if cords[1] < self._swiat.get_wysokosc() - 1:
            kierunki[0] = True
        if cords[1] > 0:
            kierunki[1] = True
        if cords[0] < self._swiat.get_szerokosc() - 1:
            kierunki[2] = True
        if cords[0] > 0:
            kierunki[3] = True
        if cords[1] < self._swiat.get_wysokosc() - 2:
            kierunki[4] = True
        if cords[1] > 1:
            kierunki[5] = True
        if cords[0] < self._swiat.get_szerokosc() - 2:
            kierunki[6] = True
        if cords[0] > 1:
            kierunki[7] = True

        ileKierunkow = 0
        for i in range (0, 8):
            if (kierunki[i]):
                ileKierunkow += 1

        kierunek = random.randint(0, ileKierunkow - 1) # index kierunku(spośród możliwych)
        licznik = -1
        index = -1
        for i in range(0, 8):
            if (kierunki[i]):
                licznik += 1
            if licznik == kierunek:
                index = i
                break

        if index == 0: # góra
            cords[1] += 1
        elif index == 1: # dół
            cords[1] -= 1
        elif index == 2: # prawo
            cords[0] += 1
        elif index == 3: # lewo
           cords[0] -= 1
        elif index == 4: # góra2
            cords[1] += 2
        elif index == 5: # dół2
            cords[1] -= 2
        elif index == 6: # prawo2
            cords[0] += 2
        elif index == 7: # lewo2
            cords[0] -= 2

    def _rozmnazanie(self, x, y):
        self._swiat.dodaj_info('Antylopy rozmnażają się.')
        dziecko = Antylopa(x, y, self._swiat, 0)
        self._swiat.get_mapa()[x][y] = dziecko
        self._swiat.get_nowo_narodzone().add(dziecko)

    def rysowanie(self):
        return (255, 204, 102)
