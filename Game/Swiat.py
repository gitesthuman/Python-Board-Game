import pygame

from Structures.Lista import Lista
from Classes.Czlowiek import Czlowiek

INFO_WIDTH = 300
FIELD_SIZE = 15


class Swiat:
    def __init__(self, wysokosc, szerokosc):
        self.__wysokosc = wysokosc
        self.__szerokosc = szerokosc
        self.__mapa = []
        self.__organizmy = Lista()
        self.__nowo_narodzone = Lista()
        self.__czlowiek = None
        self.__mapa = [[None for y in range(wysokosc)] for x in range(szerokosc)]
        self.__info = []

    def wykonaj_ture(self, screen):
        while self.__organizmy.get_current() != self.__organizmy.get_end():
            tmp = self.__organizmy.get_current()
            self.__organizmy.get_current().set_wiek(self.__organizmy.get_current().get_wiek() + 1)
            if type(tmp) is Czlowiek:
                self.__organizmy.get_current().akcja(screen)
            else:
                self.__organizmy.get_current().akcja()
            if self.__mapa[self.__czlowiek.get_X()][self.__czlowiek.get_Y()] == self.__czlowiek:
                if self.__czlowiek.umiejetnosc_trwa():
                    self.__czlowiek.specjalna_umiejetnosc()
            else:
                self.__czlowiek = None
                return
            if tmp == self.__organizmy.get_current():
                self.__organizmy.next()

        self.__organizmy.get_current().set_wiek(self.__organizmy.get_current().get_wiek() + 1)
        if type(self.__organizmy.get_current()) is Czlowiek:
            self.__organizmy.get_current().akcja(screen)
        else:
            self.__organizmy.get_current().akcja()
        if self.__mapa[self.__czlowiek.get_X()][self.__czlowiek.get_Y()] == self.__czlowiek:
            if self.__czlowiek.umiejetnosc_trwa():
                self.__czlowiek.specjalna_umiejetnosc()
        else:
            self.__czlowiek = None
            return
        if self.__organizmy.get_end() == self.__organizmy.get_current():
            self.__organizmy.next()

        while self.__nowo_narodzone.get_size() > 0:
            tmp = self.__nowo_narodzone.get_current()
            self.__organizmy.add(tmp)
            self.__nowo_narodzone.del_element(tmp.get_X(), tmp.get_Y())

    def rysuj_swiat(self, screen, info_posX, info_posY):
        screen.fill((0, 0, 0))
        INFO_FONT = pygame.font.SysFont('Arial', 14)

        # wypisz komunikaty
        for i in range(0, len(self.__info)):
            screen.blit(INFO_FONT.render(self.__info[i], True, (255, 255, 255)),
                        (info_posX + screen.get_width() - INFO_WIDTH + 2, info_posY + i * 14))

        pygame.draw.rect(screen, (150, 150, 150), pygame.Rect(0, 0, screen.get_width() - INFO_WIDTH, screen.get_height()))
        pygame.draw.rect(screen, (255, 255, 255),
                         pygame.Rect((screen.get_width() - INFO_WIDTH - self.__szerokosc * FIELD_SIZE) / 2,
                                     (screen.get_height() - 50 - self.__wysokosc * FIELD_SIZE) / 2,
                                     self.__szerokosc * FIELD_SIZE,
                                     self.__wysokosc * FIELD_SIZE))

        # rysuj mapę
        for i in range(0, self.__wysokosc):
            for j in range(0,self.__szerokosc):
                if self.__mapa[j][i] != None:
                    pygame.draw.rect(screen, self.__mapa[j][i].rysowanie(),
                                     pygame.Rect((screen.get_width() - INFO_WIDTH - self.__szerokosc * FIELD_SIZE) / 2 + j * FIELD_SIZE,
                                                 (screen.get_height() - 50 - self.__wysokosc * FIELD_SIZE) / 2 +
                                                    (self.__wysokosc - 1 - i) * FIELD_SIZE,
                                                 FIELD_SIZE,
                                                 FIELD_SIZE))

    def dodaj_organizm(self, organizm):
        self.__organizmy.add(organizm)
        self.__mapa[organizm.get_X()][organizm.get_Y()] = organizm
        if type(organizm) is Czlowiek:
            self.__czlowiek = organizm

    def get_wysokosc(self):
        return self.__wysokosc

    def get_szerokosc(self):
        return self.__szerokosc

    def get_organizmy(self):
        return self.__organizmy

    def get_nowo_narodzone(self):
        return self.__nowo_narodzone

    def get_mapa(self):
        return self.__mapa

    def get_czlowiek(self):
        return self.__czlowiek

    def koniec_swiata(self):
        if self.__czlowiek == None:
            return True
        else:
            return False

    def dodaj_info(self, info):
        self.__info.append(info)

    def wyczysc_info(self):
        self.__info = []

    def max_info(self):
        max = 0
        INFO_FONT = pygame.font.SysFont('Arial', 14)
        for i in range(0, len(self.__info)):
            if INFO_FONT.render(self.__info[i], True, (255, 255, 255)).get_width() > max:
                max = INFO_FONT.render(self.__info[i], True, (255, 255, 255)).get_width()
        return max

    def info_len(self):
        return len(self.__info) * 14