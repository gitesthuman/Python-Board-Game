import random

from Classes.Organizm import Organizm

class Zwierze(Organizm):
    def __init__(self, nazwa, X, Y, swiat, wiek, sila, inincjatywa, odporny):
        Organizm.__init__(self, nazwa, X, Y, swiat, wiek, sila, inincjatywa)
        self._odporny_na_barszcz = odporny

    def _ruch(self, x, y):
        self._swiat.get_mapa()[self._X][self._Y] = None
        self._swiat.get_organizmy().find_element(self._X, self._Y).set_X(x)
        self._swiat.get_organizmy().find_element(x, self._Y).set_Y(y)
        self._X = x
        self._Y = y
        self._swiat.get_mapa()[self._X][self._Y] = self

    def _losuj_pole(self, cords):
        kierunki = [False, False, False, False] #0-góra 1-dół 2-prawo 3-lewo

        if cords[1] < self._swiat.get_wysokosc()-1:
            kierunki[0] = True
        if cords[1] > 0:
            kierunki[1] = True
        if cords[0] < self._swiat.get_szerokosc()-1:
            kierunki[2] = True
        if cords[0] > 0:
            kierunki[3] = True

        ileKierunkow = 0
        for i in range(0, 4):
            if (kierunki[i]):
                ileKierunkow += 1

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

    def kolizja(self, napastnik):
        if self._nazwa == napastnik.get_nazwa(): #rozmnażanie
            if self._swiat.get_organizmy().find_element(self._X,self._Y) != None: # czy nie jest nowo narodzony
                kierunki = [False, False, False, False, False, False]
                x2 = napastnik.get_X()
                y2 = napastnik.get_Y()

                if self._X + 1 == napastnik.get_X() or self._X - 1 == napastnik.get_X(): # obok siebie
                    # 0-góraprawo 1-góralewo 2-dółprawo 3-dółlewo 4-prawo 5-lewo
                    if x2 > self._X:
                        if self._Y < self._swiat.get_wysokosc() - 1:
                            if self._swiat.get_mapa()[x2][self._Y + 1] == None:
                                kierunki[0] = True
                            if self._swiat.get_mapa()[self._X][self._Y + 1] == None:
                                kierunki[1] = True

                        if self._Y > 0:
                            if self._swiat.get_mapa()[x2][self._Y - 1] == None:
                                kierunki[2] = True
                            if self._swiat.get_mapa()[self._X][self._Y - 1] == None:
                                kierunki[3] = True

                        if x2 < self._swiat.get_szerokosc() - 1 and self._swiat.get_mapa()[x2 + 1][self._Y] == None:
                            kierunki[4] = True
                        if self._X > 0 and self._swiat.get_mapa()[self._X - 1][self._Y] == None:
                            kierunki[5] = True
                    else:
                        if self._Y < self._swiat.get_wysokosc() - 1:
                            if self._swiat.get_mapa()[self._X][self._Y + 1] == None:
                                kierunki[0] = True
                            if self._swiat.get_mapa()[x2][self._Y + 1] == None:
                                kierunki[1] = True

                        if self._Y > 0:
                            if self._swiat.get_mapa()[self._X][self._Y - 1] == None:
                                kierunki[2] = True
                            if self._swiat.get_mapa()[x2][self._Y - 1] == None:
                                kierunki[3] = True

                        if self._X < self._swiat.get_szerokosc() - 1 and self._swiat.get_mapa()[self._X + 1][self._Y] == None:
                            kierunki[4] = True
                        if x2 > 0 and self._swiat.get_mapa()[x2 - 1][self._Y] == None:
                            kierunki[5] = True

                else: # nad sobą
                    # 0-góra 1-dół 2-prawogóra 3-prawodół 4-lewogóra 5-lewodół
                    if y2 > self._Y:
                        if y2 < self._swiat.get_wysokosc() - 1 and self._swiat.get_mapa()[self._X][y2 + 1] == None:
                            kierunki[0] = True
                        if self._Y > 0 and self._swiat.get_mapa()[self._X][self._Y - 1] == None:
                            kierunki[1] = True
                        if self._X < self._swiat.get_szerokosc() - 1:
                            if self._swiat.get_mapa()[self._X + 1][y2] == None:
                                kierunki[2] = True
                            if self._swiat.get_mapa()[self._X + 1][self._Y] == None:
                                kierunki[3] = True

                        if self._X > 0:
                            if self._swiat.get_mapa()[self._X - 1][y2] == None:
                                kierunki[4] = True
                            if self._swiat.get_mapa()[self._X - 1][self._Y] == None:
                                kierunki[5] = True

                    else:
                        if self._Y < self._swiat.get_wysokosc() - 1 and self._swiat.get_mapa()[self._X][self._Y + 1] == None:
                            kierunki[0] = True
                        if y2 > 0 and self._swiat.get_mapa()[self._X][y2 - 1] == None:
                            kierunki[1] = True
                        if self._X < self._swiat.get_szerokosc() - 1:
                            if self._swiat.get_mapa()[self._X + 1][self._Y] == None:
                                kierunki[2] = True
                            if self._swiat.get_mapa()[self._X + 1][y2] == None:
                                kierunki[3] = True

                        if self._X > 0:
                            if self._swiat.get_mapa()[self._X - 1][self._Y] == None:
                                kierunki[4] = True
                            if self._swiat.get_mapa()[self._X - 1][y2] == None:
                                kierunki[5] = True

                ileKierunkow = 0
                for i in range(0, 6):
                    if (kierunki[i]):
                        ileKierunkow += 1

                if ileKierunkow > 0:
                    kierunek = random.randint(0, ileKierunkow - 1)  # index kierunku (spośród możliwych)
                    licznik = -1

                    for i in range(0, 6):
                        if (kierunki[i]):
                            licznik += 1
                        if licznik == kierunek:
                            index = i
                            break

                    if self._X + 1 == napastnik.get_X() or self._X - 1 == napastnik.get_X():
                        if index == 0:# góraprawo
                            if x2 > self._X:
                                self._rozmnazanie(x2, self._Y + 1)
                            else:
                                self._rozmnazanie(self._X, self._Y + 1)

                        if index == 1:# góralewo
                            if x2 > self._X:
                                self._rozmnazanie(self._X, self._Y + 1)
                            else:
                                self._rozmnazanie(x2, self._Y)

                        if index == 2:# dółprawo
                            if x2 > self._X:
                                self._rozmnazanie(x2, self._Y - 1)
                            else:
                                self._rozmnazanie(self._X, self._Y - 1)

                        if index == 3:# dółlewo
                            if x2 > self._X:
                                self._rozmnazanie(self._X, self._Y - 1)
                            else:
                                self._rozmnazanie(x2, self._Y - 1)

                        if index == 4:# prawo
                            if x2 > self._X:
                                self._rozmnazanie(x2 + 1, self._Y)
                            else:
                                self._rozmnazanie(self._X + 1, self._Y)

                        if index == 5:# lewo
                            if x2 > self._X:
                                self._rozmnazanie(self._X - 1, self._Y)
                            else:
                                self._rozmnazanie(x2 - 1, self._Y)

                    else:
                        if index == 0:# góra
                            if y2 > self._X:
                                self._rozmnazanie(self._X, y2 + 1);
                            else:
                                self._rozmnazanie(self._X, self._Y + 1)

                        if index == 1:# dół
                            if y2 > self._X:
                                self._rozmnazanie(self._X, self._Y - 1)
                            else:
                                self._rozmnazanie(self._X, y2 - 1)

                        if index == 2:# prawogóra
                            if y2 > self._X:
                                self._rozmnazanie(self._X + 1, y2)
                            else:
                                self._rozmnazanie(self._X + 1, self._Y)

                        if index == 3:# prawodół
                            if y2 > self._Y:
                                self._rozmnazanie(self._X + 1, self._Y)
                            else:
                                self._rozmnazanie(self._X + 1, y2)

                        if index == 4:# lewogóra
                            if y2 > self._Y:
                                self._rozmnazanie(self._X - 1, y2)
                            else:
                                self._rozmnazanie(self._X - 1, self._Y)

                        if index == 5:# lewodół
                            if y2 > self._Y:
                                self._rozmnazanie(self._X - 1, self._Y)
                            else:
                                self._rozmnazanie(self._X - 1, y2)

        else: # walka
            info = 'Fight! ' + napastnik.get_nazwa() + ' attacks ' + self._nazwa + '! '
            if napastnik.get_sila() >= self._sila:
                info += napastnik.get_nazwa() + ' (strength ' + str(napastnik.get_sila()) \
                        + ') defeats ' + self._nazwa + ' (strength ' + str(self._sila) + ')!'
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

            else:
                info += self._nazwa + ' (strength ' + str(self._sila) + ') defeats ' \
                        + napastnik.get_nazwa() + ' (strength ' + str(napastnik.get_sila()) + ')!'
                self._swiat.get_mapa()[napastnik.get_X()][napastnik.get_Y()] = None
                if self._swiat.get_organizmy().find_element(napastnik.get_X(), napastnik.get_Y()):
                    self._swiat.get_organizmy().del_element(napastnik.get_X(), napastnik.get_Y())
                else:
                    self._swiat.get_nowo_narodzone().del_element(napastnik.get_X(), napastnik.get_Y())
            self._swiat.dodaj_info(info)

    def akcja(self):
        cords = [self._X, self._Y]
        self._losuj_pole(cords)

        if cords[0] != self._X or cords[1] != self._Y:
            if self._swiat.get_mapa()[cords[0]][cords[1]] == None:
                self._ruch(cords[0], cords[1])
            else:
                self._swiat.get_mapa()[cords[0]][cords[1]].kolizja(self)

    def odporny(self):
        return self._odporny_na_barszcz
