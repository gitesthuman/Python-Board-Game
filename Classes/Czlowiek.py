import pygame
import sys

from Classes.Zwierze import Zwierze


class Czlowiek(Zwierze):
    def __init__(self, X, Y, swiat, wiek, czas_trwania_umiejetnosci, cool_down_umiejetnosci):
        Zwierze.__init__(self, 'Human', X, Y, swiat, wiek, 5, 4, False)
        self.__czas_trwania_umiejetnosci = czas_trwania_umiejetnosci
        self.__cool_down_umiejetnosci = cool_down_umiejetnosci

    def akcja(self, screen):
        if self.__czas_trwania_umiejetnosci > 0:
            self.__czas_trwania_umiejetnosci -= 1
        elif self.__cool_down_umiejetnosci > 0:
            self.__cool_down_umiejetnosci -= 1

        ruch = False
        x = self._X
        y = self._Y
        scrollX = 0
        scrollY = 0
        while not ruch:
            mouse = pygame.mouse.get_pos()
            self._swiat.rysuj_swiat(screen, scrollX, scrollY)
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    sys.exit(0)
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_UP and y < self._swiat.get_wysokosc() - 1:  # ruch w górę
                        y += 1
                        ruch = True
                    elif ev.key == pygame.K_DOWN and y > 0:  # ruch w dół
                        y -= 1
                        ruch = True
                    elif ev.key == pygame.K_RIGHT and x < self._swiat.get_szerokosc() - 1:  # ruch w prawo
                        x += 1
                        ruch = True
                    elif ev.key == pygame.K_LEFT and x > 0:  # ruch w lewo
                        x -= 1
                        ruch = True
                    elif ev.key == pygame.K_x and \
                            self.__czas_trwania_umiejetnosci == 0 and \
                            self.__cool_down_umiejetnosci == 0: # super umiejętność
                        self.__czas_trwania_umiejetnosci = 5
                        self.__cool_down_umiejetnosci = 5
                        self._swiat.dodaj_info('Holocaust activated!')
                        self._swiat.rysuj_swiat(screen, scrollX, scrollY)

                if ev.type == pygame.MOUSEBUTTONDOWN: # przesuwanie zawartości komunikatów
                    if ev.button == 1:
                        if screen.get_width() - 300 <= mouse[0] <= screen.get_width() and self._swiat.max_info() > 300:
                            scrollX += 50
                            if scrollX > 0:
                                scrollX = 0
                    elif ev.button == 3:
                        if screen.get_width() - 300 <= mouse[0] <= screen.get_width() and self._swiat.max_info() > 300:
                            scrollX -= 50
                            if scrollX < 300 - self._swiat.max_info() - 5:
                                scrollX = 300 - self._swiat.max_info() - 5
                    elif ev.button == 4:
                        if screen.get_width() - 500 <= mouse[0] <= screen.get_width() and self._swiat.info_len() > screen.get_height():
                            scrollY += 50
                            if scrollY > 0:
                                scrollY = 0
                    elif ev.button == 5:
                        if screen.get_width() - 500 <= mouse[0] <= screen.get_width() and self._swiat.info_len() > screen.get_height():
                            scrollY -= 50
                            if scrollY < screen.get_height() - self._swiat.info_len() - 5:
                                scrollY = screen.get_height() - self._swiat.info_len() - 5

            pygame.display.update()

        self._swiat.wyczysc_info()

        if self._swiat.get_mapa()[x][y] == None:
            self._ruch(x, y)
        else:
            self._swiat.get_mapa()[x][y].kolizja(self)

    def umiejetnosc_trwa(self):
        if self.__czas_trwania_umiejetnosci > 0:
            return True
        else:
            return False

    def pal(self, x, y):
        info = 'Human burns ' + self._swiat.get_mapa()[x][y].get_nazwa() + '!'
        self._swiat.dodaj_info(info)

        if (self._swiat.get_organizmy().find_element(x, y)):
            self._swiat.get_organizmy().del_element(x, y)
        else:
            self._swiat.get_nowo_narodzone().del_element(x, y)
        self._swiat.get_mapa()[x][y] = None

    def specjalna_umiejetnosc(self):
        if self._Y < self._swiat.get_wysokosc() - 1 and self._swiat.get_mapa()[self._X][self._Y + 1] != None:
            self.pal(self._X, self._Y + 1)
        if self._Y > 0 and self._swiat.get_mapa()[self._X][self._Y - 1] != None:
            self.pal(self._X, self._Y - 1)
        if self._X < self._swiat.get_szerokosc() - 1 and self._swiat.get_mapa()[self._X + 1][self._Y] != None:
            self.pal(self._X + 1, self._Y)
        if self._X > 0 and self._swiat.get_mapa()[self._X - 1][self._Y] != None:
            self.pal(self._X - 1, self._Y)

    def get_czas_trwania_umiejetnosci(self):
        return self.__czas_trwania_umiejetnosci

    def get_cool_down_umiejetnosci(self):
        return self.__cool_down_umiejetnosci

    def rysowanie(self):
        return 0, 0, 255
