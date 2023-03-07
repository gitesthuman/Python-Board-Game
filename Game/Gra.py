import math
import random
import re
import os.path
import sys

from Game.Swiat import *
from Classes.Antylopa import Antylopa
from Classes.BarszczSosnowskiego import BarszczSosnowskiego
from Classes.CyberOwca import CyberOwca
from Classes.Czlowiek import Czlowiek
from Classes.Guarana import Guarana
from Classes.Lis import Lis
from Classes.Mlecz import Mlecz
from Classes.Owca import Owca
from Classes.Trawa import Trawa
from Classes.WilczeJagody import WilczeJagody
from Classes.Wilk import Wilk
from Classes.Zolw import Zolw
from Classes.Zwierze import Zwierze

MIN_SCREEN_WIDTH = 280
MIN_SCREEN_HEIGHT = 400


class Gra:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("The Organisms 2.0")
        self.__nowyswiat = None

    def __wczytaj(self, sciezka):
        while not os.path.exists(sciezka):
            sciezka = input("Podaj poprawna sciezke pliku: ")
        plik = open(sciezka, "r")

        linia = plik.readline()
        wymiary = linia.split(' ')
        N = int(wymiary[0])
        M = int(wymiary[1])
        del self.__nowyswiat
        self.__nowyswiat = Swiat(N, M)

        for linia in plik.readlines():
            elem = linia.split(' ')
            nazwa, x, y, wiek = str(elem[0]), int(elem[1]), int(elem[2]), int(elem[3])

            if nazwa == "Antylopa":
                organizm = Antylopa(x, y, self.__nowyswiat, wiek)
            elif nazwa == "BarszczSosnowskiego":
                organizm = BarszczSosnowskiego(x, y, self.__nowyswiat, wiek)
            elif nazwa == "CyberOwca":
                organizm = CyberOwca(x, y, self.__nowyswiat, wiek)
            elif nazwa == "Człowiek":
                sila, czas, cd = int(elem[4]), int(elem[5]), int(elem[6])
                organizm = Czlowiek(x, y, self.__nowyswiat, wiek, czas, cd)
                organizm.set_sila(sila)
                self.__nowyswiat.dodaj_organizm(organizm)
                continue
            elif nazwa == "Guarana":
                organizm = Guarana(x, y, self.__nowyswiat, wiek)
            elif nazwa == "Lis":
                organizm = Lis(x, y, self.__nowyswiat, wiek)
            elif nazwa == "Mlecz":
                organizm = Mlecz(x, y, self.__nowyswiat, wiek)
            elif nazwa == "Owca":
                organizm = Owca(x, y, self.__nowyswiat, wiek)
            elif nazwa == "Trawa":
                organizm = Trawa(x, y, self.__nowyswiat, wiek)
            elif nazwa == "WilczeJagody":
                organizm = WilczeJagody(x, y, self.__nowyswiat, wiek)
            elif nazwa == "Wilk":
                organizm = Wilk(x, y, self.__nowyswiat, wiek)
            elif nazwa == "Żółw":
                organizm = Zolw(x, y, self.__nowyswiat, wiek)

            if isinstance(organizm, Zwierze):
                organizm.set_sila(int(elem[4]))
            self.__nowyswiat.dodaj_organizm(organizm)

        plik.close()

    def __obok_czlowieka(self, cords, czlowiek):
        if abs(cords[0] - czlowiek[0]) <= 1 and abs(cords[1] - czlowiek[1]) <= 1:
            return True
        else:
            return False

    def __losuj(self, swiat, czlowiek):
        cords = [0, 0]
        cords[0] = random.randint(0, swiat.get_szerokosc() - 1)
        cords[1] = random.randint(0, swiat.get_wysokosc() - 1)
        while swiat.get_mapa()[cords[0]][cords[1]] != None or self.__obok_czlowieka(cords, czlowiek):
            cords[0] = random.randint(0, swiat.get_szerokosc() - 1)
            cords[1] = random.randint(0, swiat.get_wysokosc() - 1)
        return cords

    def __generuj(self):
        MINIMAL = 97 # minimalny rozmiar świata
        ILE_GATUNKOW = 11 # liczba gatunków (bez człowieka)
        HUMAN = 9 # miejsce dla człowieka

        screen = pygame.display.set_mode((600, 400))
        white = (255, 255, 255)
        color_light = (130, 130, 130)
        color_dark = (100, 100, 100)
        font1 = pygame.font.SysFont('Arial', 18)

        szer = ''
        wys = ''
        szer_napis = font1.render('Podaj szerokość świata: ', True, white)
        wys_napis = font1.render('Podaj wysokość świata: ', True, white)
        zatwierdzone = False

        while not zatwierdzone:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    sys.exit()
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_0 and len(szer) > 0:
                        szer += '0'
                    elif ev.key == pygame.K_1:
                        szer += '1'
                    elif ev.key == pygame.K_2:
                        szer += '2'
                    elif ev.key == pygame.K_3:
                        szer += '3'
                    elif ev.key == pygame.K_4:
                        szer += '4'
                    elif ev.key == pygame.K_5:
                        szer += '5'
                    elif ev.key == pygame.K_6:
                        szer += '6'
                    elif ev.key == pygame.K_7:
                        szer += '7'
                    elif ev.key == pygame.K_8:
                        szer += '8'
                    elif ev.key == pygame.K_9:
                        szer += '9'
                    elif ev.key == pygame.K_BACKSPACE:
                        szer = szer[:-1]
                    elif ev.key == pygame.K_RETURN and len(szer) > 0:
                        zatwierdzone = True

            screen.fill((100, 100, 100))

            screen.blit(szer_napis, (50, 100))
            szer_wart = font1.render(szer, True, white)
            screen.blit(szer_wart, (50 + szer_napis.get_width() + 10, 100))
            pygame.display.update()

        zatwierdzone = False
        while not zatwierdzone:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    sys.exit()
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_0 and len(wys) > 0:
                        wys += '0'
                    elif ev.key == pygame.K_1:
                        wys += '1'
                    elif ev.key == pygame.K_2:
                        wys += '2'
                    elif ev.key == pygame.K_3:
                        wys += '3'
                    elif ev.key == pygame.K_4:
                        wys += '4'
                    elif ev.key == pygame.K_5:
                        wys += '5'
                    elif ev.key == pygame.K_6:
                        wys += '6'
                    elif ev.key == pygame.K_7:
                        wys += '7'
                    elif ev.key == pygame.K_8:
                        wys += '8'
                    elif ev.key == pygame.K_9:
                        wys += '9'
                    elif ev.key == pygame.K_BACKSPACE:
                        wys = wys[:-1]
                    elif ev.key == pygame.K_RETURN and len(szer) > 0:
                        zatwierdzone = True

            screen.fill((100, 100, 100))

            screen.blit(szer_napis, (50, 100))
            szer_wart = font1.render(szer, True, white)
            screen.blit(szer_wart, (50 + szer_napis.get_width() + 10, 100))
            screen.blit(wys_napis, (50, 200))
            wys_wart = font1.render(wys, True, white)
            screen.blit(wys_wart, (50 + szer_napis.get_width() + 10, 200))
            pygame.display.update()

        M = int(szer)
        N = int(wys)
        while N * M < MINIMAL:
            szer = ''
            wys = ''
            komunikat = font1.render('Zbyt mały świat!', True, white)
            zatwierdzone = False

            while not zatwierdzone:
                for ev in pygame.event.get():
                    if ev.type == pygame.QUIT:
                        sys.exit()
                    if ev.type == pygame.KEYDOWN:
                        if ev.key == pygame.K_0 and len(szer) > 0:
                            szer += '0'
                        elif ev.key == pygame.K_1:
                            szer += '1'
                        elif ev.key == pygame.K_2:
                            szer += '2'
                        elif ev.key == pygame.K_3:
                            szer += '3'
                        elif ev.key == pygame.K_4:
                            szer += '4'
                        elif ev.key == pygame.K_5:
                            szer += '5'
                        elif ev.key == pygame.K_6:
                            szer += '6'
                        elif ev.key == pygame.K_7:
                            szer += '7'
                        elif ev.key == pygame.K_8:
                            szer += '8'
                        elif ev.key == pygame.K_9:
                            szer += '9'
                        elif ev.key == pygame.K_BACKSPACE:
                            szer = szer[:-1]
                        elif ev.key == pygame.K_RETURN and len(szer) > 0:
                            zatwierdzone = True

                screen.fill((100, 100, 100))
                screen.blit(komunikat, (250 , 30))
                screen.blit(szer_napis, (50, 100))
                szer_wart = font1.render(szer, True, white)
                screen.blit(szer_wart, (50 + szer_napis.get_width() + 10, 100))
                pygame.display.update()

            zatwierdzone = False
            while not zatwierdzone:
                for ev in pygame.event.get():
                    if ev.type == pygame.QUIT:
                        sys.exit()
                    if ev.type == pygame.KEYDOWN:
                        if ev.key == pygame.K_0 and len(wys) > 0:
                            wys += '0'
                        elif ev.key == pygame.K_1:
                            wys += '1'
                        elif ev.key == pygame.K_2:
                            wys += '2'
                        elif ev.key == pygame.K_3:
                            wys += '3'
                        elif ev.key == pygame.K_4:
                            wys += '4'
                        elif ev.key == pygame.K_5:
                            wys += '5'
                        elif ev.key == pygame.K_6:
                            wys += '6'
                        elif ev.key == pygame.K_7:
                            wys += '7'
                        elif ev.key == pygame.K_8:
                            wys += '8'
                        elif ev.key == pygame.K_9:
                            wys += '9'
                        elif ev.key == pygame.K_BACKSPACE:
                            wys = wys[:-1]
                        elif ev.key == pygame.K_RETURN and len(wys) > 0:
                            zatwierdzone = True

                screen.fill((100, 100, 100))

                screen.blit(komunikat, (250, 30))
                screen.blit(szer_napis, (50, 100))
                szer_wart = font1.render(szer, True, white)
                screen.blit(szer_wart, (50 + szer_napis.get_width() + 10, 100))
                screen.blit(wys_napis, (50, 200))
                wys_wart = font1.render(wys, True, white)
                screen.blit(wys_wart, (50 + szer_napis.get_width() + 10, 200))
                pygame.display.update()

            M = int(szer)
            N = int(wys)

        del self.__nowyswiat
        self.__nowyswiat = Swiat(N, M)
        Cords = [0, 0]
        Cords[0] = random.randint(0, M - 1)
        Cords[1] = random.randint(0, N - 1)
        self.__nowyswiat.dodaj_organizm(Czlowiek(Cords[0], Cords[1], self.__nowyswiat, 0, 0, 0))
        populacjaGatunku = math.floor((N * M * 0.3 - HUMAN) / ILE_GATUNKOW)

        cords = [0, 0]
        for i in range(0, populacjaGatunku):
            cords = self.__losuj(self.__nowyswiat, Cords)
            self.__nowyswiat.dodaj_organizm(Antylopa(cords[0], cords[1], self.__nowyswiat, 0))
            cords = self.__losuj(self.__nowyswiat, Cords)
            self.__nowyswiat.dodaj_organizm(BarszczSosnowskiego(cords[0], cords[1], self.__nowyswiat, 0))
            cords = self.__losuj(self.__nowyswiat, Cords)
            self.__nowyswiat.dodaj_organizm(CyberOwca(cords[0], cords[1], self.__nowyswiat, 0))
            cords = self.__losuj(self.__nowyswiat, Cords)
            self.__nowyswiat.dodaj_organizm(Guarana(cords[0], cords[1], self.__nowyswiat, 0))
            cords = self.__losuj(self.__nowyswiat, Cords)
            self.__nowyswiat.dodaj_organizm(Lis(cords[0], cords[1], self.__nowyswiat, 0))
            cords = self.__losuj(self.__nowyswiat, Cords)
            self.__nowyswiat.dodaj_organizm(Mlecz(cords[0], cords[1], self.__nowyswiat, 0))
            cords = self.__losuj(self.__nowyswiat, Cords)
            self.__nowyswiat.dodaj_organizm(Owca(cords[0], cords[1], self.__nowyswiat, 0))
            cords = self.__losuj(self.__nowyswiat, Cords)
            self.__nowyswiat.dodaj_organizm(Trawa(cords[0], cords[1], self.__nowyswiat, 0))
            cords = self.__losuj(self.__nowyswiat, Cords)
            self.__nowyswiat.dodaj_organizm(WilczeJagody(cords[0], cords[1], self.__nowyswiat, 0))
            cords = self.__losuj(self.__nowyswiat, Cords)
            self.__nowyswiat.dodaj_organizm(Wilk(cords[0], cords[1], self.__nowyswiat, 0))
            cords = self.__losuj(self.__nowyswiat, Cords)
            self.__nowyswiat.dodaj_organizm(Zolw(cords[0], cords[1], self.__nowyswiat, 0))

    def __zapisz(self, sciezka):
        plik = open(sciezka, "w")
        plik.write(str(self.__nowyswiat.get_wysokosc()))
        plik.write(" ")
        plik.write(str(self.__nowyswiat.get_szerokosc()))
        plik.write("\n")

        for i in range(0, self.__nowyswiat.get_organizmy().get_size()):
            organizm = self.__nowyswiat.get_organizmy().get_current()
            nazwa = organizm.get_nazwa()
            nazwa = re.sub(r"\s+", "", nazwa, flags=re.UNICODE) # usuwanie spacji z nazwy

            plik.write(nazwa+" ")
            plik.write(str(organizm.get_X()))
            plik.write(" ")
            plik.write(str(organizm.get_Y()))
            plik.write(" ")
            plik.write(str(organizm.get_wiek()))

            if isinstance(organizm, Zwierze):
                plik.write(" ")
                plik.write(str(organizm.get_sila()))

                if type(organizm) is Czlowiek:
                    plik.write(" ")
                    plik.write(str(organizm.get_czas_trwania_umiejetnosci()))
                    plik.write(" ")
                    plik.write(str(organizm.get_cool_down_umiejetnosci()))

            plik.write("\n")
            self.__nowyswiat.get_organizmy().next()

        plik.close()

    def __graj(self):
        screen = pygame.display.set_mode((max(MIN_SCREEN_WIDTH , 100 + self.__nowyswiat.get_szerokosc() * FIELD_SIZE) + INFO_WIDTH,
                                          max(MIN_SCREEN_HEIGHT, 100 + self.__nowyswiat.get_wysokosc() * FIELD_SIZE)))
        width = screen.get_width()
        height = screen.get_height()

        while not self.__nowyswiat.koniec_swiata():
            scrollX = 0
            scrollY = 0
            pygame.display.update()

            white = (255, 255, 255)
            color_light = (130, 130, 130)
            color_dark = (100, 100, 100)
            font1 = pygame.font.SysFont('Arial', 20)

            zapisz = font1.render('Zapisz', True, white)
            dalej = font1.render('Dalej', True, white)
            menu = font1.render('Menu', True, white)
            akcja = False
            while not akcja:
                self.__nowyswiat.rysuj_swiat(screen, scrollX, scrollY)
                mouse = pygame.mouse.get_pos()

                for ev in pygame.event.get():
                    if ev.type == pygame.QUIT:
                        sys.exit(0)
                    if ev.type == pygame.MOUSEBUTTONDOWN:
                        if ev.button == 1:
                            if 30 <= mouse[0] <= 90 and height - 50 <= mouse[1] <= height - 20: # zapis
                                sciezka = ''
                                zatwierdzone = False
                                komunikat = font1.render("Podaj ścieżkę pliku: ", True, white)

                                while not zatwierdzone:
                                    for ev in pygame.event.get():
                                        if ev.type == pygame.QUIT:
                                            sys.exit(0)
                                        if ev.type == pygame.KEYDOWN:
                                            if ev.key == pygame.K_BACKSPACE:
                                                sciezka = sciezka[:-1]
                                            elif ev.key == pygame.K_RETURN:
                                                if len(sciezka) > 0:
                                                    zatwierdzone = True
                                            else:
                                                sciezka += ev.unicode

                                    pygame.draw.rect(screen, color_dark, pygame.Rect(width / 2 - 150, height / 2 - 50, 300, 100))
                                    screen.blit(komunikat, (width / 2 - 145, height / 2 - 45))
                                    wart = font1.render(sciezka, True, white)
                                    screen.blit(wart, (width / 2 - 145, height / 2))
                                    pygame.display.update()
                                self.__zapisz(sciezka)
                                self.__nowyswiat.rysuj_swiat(screen, scrollX, scrollY)

                            elif 110 <= mouse[0] <= 170 and height - 50 <= mouse[1] <= height - 20: # dalej
                                akcja = True
                            elif 190 <= mouse[0] <= 250 and height - 50 <= mouse[1] <= height - 20: # menu
                                self.start()

                            elif width - INFO_WIDTH <= mouse[0] <= width and self.__nowyswiat.max_info() > INFO_WIDTH: # przesuwanie zawartości komunikatów
                                scrollX += 50
                                if scrollX > 0:
                                    scrollX = 0

                        elif ev.button == 3:
                            if width - INFO_WIDTH <= mouse[0] <= width and self.__nowyswiat.max_info() > INFO_WIDTH: # przesuwanie zawartości komunikatów
                                scrollX -= 50
                                if scrollX < INFO_WIDTH - self.__nowyswiat.max_info() - 5:
                                    scrollX = INFO_WIDTH - self.__nowyswiat.max_info() - 5

                            elif (width - INFO_WIDTH - self.__nowyswiat.get_szerokosc() * FIELD_SIZE) / 2 <= mouse[0] \
                                        <= (width - INFO_WIDTH - self.__nowyswiat.get_szerokosc() * FIELD_SIZE) / 2 + self.__nowyswiat.get_szerokosc() * FIELD_SIZE and \
                                    (height - 50 - self.__nowyswiat.get_wysokosc() * FIELD_SIZE) / 2 <= mouse[1] \
                                        <= (height - 50 - self.__nowyswiat.get_wysokosc() * FIELD_SIZE) / 2 + self.__nowyswiat.get_wysokosc() * FIELD_SIZE:
                                # indexy na mapie
                                indexX = math.floor((mouse[0] - (width - INFO_WIDTH - self.__nowyswiat.get_szerokosc() * FIELD_SIZE) / 2) / FIELD_SIZE)
                                indexY = self.__nowyswiat.get_wysokosc() - 1 - math.floor((mouse[1] - (height - 50 - self.__nowyswiat.get_wysokosc() * FIELD_SIZE) / 2) / FIELD_SIZE)

                                if self.__nowyswiat.get_mapa()[indexX][indexY] == None: # dodaj organizm
                                    posX = mouse[0]
                                    posY = mouse[1]
                                    dodano = False
                                    black = (0, 0, 0)
                                    smallfont = pygame.font.SysFont('Arial', 12)

                                    dodaj = smallfont.render('Dodaj organizm:', True, black)
                                    antylopa = smallfont.render('Antylopa', True, black)
                                    barszcz = smallfont.render('Barszcz Sosnowskiego', True, black)
                                    cyber = smallfont.render('Cyber Owca', True, black)
                                    guarana = smallfont.render('Guarana', True, black)
                                    lis = smallfont.render('Lis', True, black)
                                    mlecz = smallfont.render('Mlecz', True, black)
                                    owca = smallfont.render('Owca', True, black)
                                    trawa = smallfont.render('Trawa', True, black)
                                    jagody = smallfont.render('Wilcze Jagody', True, black)
                                    wilk = smallfont.render('Wilk', True, black)
                                    zolw = smallfont.render('Żółw', True, black)

                                    while not dodano:
                                        mouse = pygame.mouse.get_pos()

                                        pygame.draw.rect(screen, color_dark, pygame.Rect(posX, posY, 100, 12))

                                        if posX <= mouse[0] < posX + 100 and posY + 12 <= mouse[1] < posY + 24:
                                            pygame.draw.rect(screen, color_light, pygame.Rect(posX, posY + 12, 100, 12))
                                        else:
                                            pygame.draw.rect(screen, color_dark, pygame.Rect(posX, posY + 12, 100, 12))

                                        if posX <= mouse[0] < posX + 100 and posY + 24 <= mouse[1] < posY + 36:
                                            pygame.draw.rect(screen, color_light, pygame.Rect(posX, posY + 24, 100, 12))
                                        else:
                                            pygame.draw.rect(screen, color_dark, pygame.Rect(posX, posY + 24, 100, 12))

                                        if posX <= mouse[0] < posX + 100 and posY + 36 <= mouse[1] < posY + 48:
                                            pygame.draw.rect(screen, color_light, pygame.Rect(posX, posY + 36, 100, 12))
                                        else:
                                            pygame.draw.rect(screen, color_dark, pygame.Rect(posX, posY + 36, 100, 12))

                                        if posX <= mouse[0] < posX + 100 and posY + 48 <= mouse[1] < posY + 60:
                                            pygame.draw.rect(screen, color_light, pygame.Rect(posX, posY + 48, 100, 12))
                                        else:
                                            pygame.draw.rect(screen, color_dark, pygame.Rect(posX, posY + 48, 100, 12))

                                        if posX <= mouse[0] < posX + 100 and posY + 60 <= mouse[1] < posY + 72:
                                            pygame.draw.rect(screen, color_light, pygame.Rect(posX, posY + 60, 100, 12))
                                        else:
                                            pygame.draw.rect(screen, color_dark, pygame.Rect(posX, posY + 60, 100, 12))

                                        if posX <= mouse[0] < posX + 100 and posY + 72 <= mouse[1] < posY + 84:
                                            pygame.draw.rect(screen, color_light, pygame.Rect(posX, posY + 72, 100, 12))
                                        else:
                                            pygame.draw.rect(screen, color_dark, pygame.Rect(posX, posY + 72, 100, 12))

                                        if posX <= mouse[0] < posX + 100 and posY + 84 <= mouse[1] < posY + 96:
                                            pygame.draw.rect(screen, color_light, pygame.Rect(posX, posY + 84, 100, 12))
                                        else:
                                            pygame.draw.rect(screen, color_dark, pygame.Rect(posX, posY + 84, 100, 12))

                                        if posX <= mouse[0] < posX + 100 and posY + 96 <= mouse[1] < posY + 108:
                                            pygame.draw.rect(screen, color_light, pygame.Rect(posX, posY + 96, 100, 12))
                                        else:
                                            pygame.draw.rect(screen, color_dark, pygame.Rect(posX, posY + 96, 100, 12))

                                        if posX <= mouse[0] < posX + 100 and posY + 108 <= mouse[1] < posY + 120:
                                            pygame.draw.rect(screen, color_light, pygame.Rect(posX, posY + 108, 100, 12))
                                        else:
                                            pygame.draw.rect(screen, color_dark, pygame.Rect(posX, posY + 108, 100, 12))

                                        if posX <= mouse[0] < posX + 100 and posY + 120 <= mouse[1] < posY + 132:
                                            pygame.draw.rect(screen, color_light, pygame.Rect(posX, posY + 120, 100, 12))
                                        else:
                                            pygame.draw.rect(screen, color_dark, pygame.Rect(posX, posY + 120, 100, 12))

                                        if posX <= mouse[0] < posX + 100 and posY + 132 <= mouse[1] < posY + 144:
                                            pygame.draw.rect(screen, color_light, pygame.Rect(posX, posY + 132, 100, 12))
                                        else:
                                            pygame.draw.rect(screen, color_dark, pygame.Rect(posX, posY + 132, 100, 12))

                                        for ev in pygame.event.get():
                                            if ev.type == pygame.QUIT:
                                                sys.exit(0)
                                            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1: # dodanie (rzeczywiste kliknięcie)
                                                if posX <= mouse[0] < posX + 100 and posY + 12 <= mouse[1] < posY + 24:
                                                    self.__nowyswiat.dodaj_organizm(Antylopa(indexX, indexY, self.__nowyswiat, 0))

                                                elif posX <= mouse[0] < posX + 100 and posY + 24 <= mouse[1] < posY + 36:
                                                    self.__nowyswiat.dodaj_organizm(BarszczSosnowskiego(indexX, indexY, self.__nowyswiat, 0))

                                                elif posX <= mouse[0] < posX + 100 and posY + 36 <= mouse[1] < posY + 48:
                                                    self.__nowyswiat.dodaj_organizm(CyberOwca(indexX, indexY, self.__nowyswiat, 0))

                                                elif posX <= mouse[0] < posX + 100 and posY + 48 <= mouse[1] < posY + 60:
                                                    self.__nowyswiat.dodaj_organizm(Guarana(indexX, indexY, self.__nowyswiat, 0))

                                                elif posX <= mouse[0] < posX + 100 and posY + 60 <= mouse[1] < posY + 72:
                                                    self.__nowyswiat.dodaj_organizm(Lis(indexX, indexY, self.__nowyswiat, 0))

                                                elif posX <= mouse[0] < posX + 100 and posY + 72 <= mouse[1] < posY + 84:
                                                    self.__nowyswiat.dodaj_organizm(Mlecz(indexX, indexY, self.__nowyswiat, 0))

                                                elif posX <= mouse[0] < posX + 100 and posY + 84 <= mouse[1] < posY + 96:
                                                    self.__nowyswiat.dodaj_organizm(Owca(indexX, indexY, self.__nowyswiat, 0))

                                                elif posX <= mouse[0] < posX + 100 and posY + 96 <= mouse[1] < posY + 108:
                                                    self.__nowyswiat.dodaj_organizm(Trawa(indexX, indexY, self.__nowyswiat, 0))

                                                elif posX <= mouse[0] < posX + 100 and posY + 108 <= mouse[1] < posY + 120:
                                                    self.__nowyswiat.dodaj_organizm(WilczeJagody(indexX, indexY, self.__nowyswiat, 0))

                                                elif posX <= mouse[0] < posX + 100 and posY + 120 <= mouse[1] < posY + 132:
                                                    self.__nowyswiat.dodaj_organizm(Wilk(indexX, indexY, self.__nowyswiat, 0))

                                                elif posX <= mouse[0] < posX + 100 and posY + 132 <= mouse[1] < posY + 144:
                                                    self.__nowyswiat.dodaj_organizm(Zolw(indexX, indexY, self.__nowyswiat, 0))

                                                dodano = True

                                            elif ev.type == pygame.MOUSEBUTTONDOWN:
                                                dodano = True

                                        screen.blit(dodaj, (posX, posY))
                                        screen.blit(antylopa, (posX, posY + 12))
                                        screen.blit(barszcz, (posX, posY + 24))
                                        screen.blit(cyber, (posX, posY + 36))
                                        screen.blit(guarana, (posX, posY + 48))
                                        screen.blit(lis, (posX, posY + 60))
                                        screen.blit(mlecz, (posX, posY + 72))
                                        screen.blit(owca, (posX, posY + 84))
                                        screen.blit(trawa, (posX, posY + 96))
                                        screen.blit(jagody, (posX, posY + 108))
                                        screen.blit(wilk, (posX, posY + 120))
                                        screen.blit(zolw, (posX, posY + 132))

                                        pygame.display.update()

                        # przesuwanie zawartości komunikatów
                        elif ev.button == 4:
                            if width - INFO_WIDTH <= mouse[0] <= width and self.__nowyswiat.info_len() > height:
                                scrollY += 50
                                if scrollY > 0:
                                    scrollY = 0
                        elif ev.button == 5:
                            if width - INFO_WIDTH <= mouse[0] <= width and self.__nowyswiat.info_len() > height:
                                scrollY -= 50
                                if scrollY < height - self.__nowyswiat.info_len() - 5:
                                    scrollY = height - self.__nowyswiat.info_len() - 5

                if 30 <= mouse[0] <= 90 and height - 50 <= mouse[1] <= height - 20:
                    pygame.draw.rect(screen, color_light, pygame.Rect(30, height - 50, 60, 30))
                else:
                    pygame.draw.rect(screen, color_dark, pygame.Rect(30, height - 50, 60, 30))

                if 110 <= mouse[0] <= 170 and height - 50 <= mouse[1] <= height - 20:
                    pygame.draw.rect(screen, color_light, pygame.Rect(110, height - 50, 60, 30))
                else:
                    pygame.draw.rect(screen, color_dark, pygame.Rect(110, height - 50, 60, 30))

                if 190 <= mouse[0] <= 250 and height - 50 <= mouse[1] <= height - 20:
                    pygame.draw.rect(screen, color_light, pygame.Rect(190, height - 50, 60, 30))
                else:
                    pygame.draw.rect(screen, color_dark, pygame.Rect(190, height - 50, 60, 30))

                screen.blit(zapisz, (30 + (60 - zapisz.get_width()) / 2, height - 50 + (30 - zapisz.get_height()) / 2))
                screen.blit(dalej, (110 + (60 - dalej.get_width()) / 2, height - 50 + (30 - dalej.get_height()) / 2))
                screen.blit(menu, (190 + (60 - menu.get_width()) / 2, height - 50 + (30 - menu.get_height()) / 2))
                pygame.display.update()

            self.__nowyswiat.wyczysc_info()
            self.__nowyswiat.wykonaj_ture(screen)

        self.__nowyswiat.dodaj_info('Człowiek umarł...')
        self.__nowyswiat.rysuj_swiat(screen, 0, 0)

        koniec = pygame.font.SysFont('Arial black', 20).render('KONIEC GRY', True, white)
        gra = font1.render('Zagraj jeszcze raz', True, white)
        wyjscie = font1.render('Wyjście', True, white)

        while True:
            mouse = pygame.mouse.get_pos()
            pygame.draw.rect(screen, (90, 90, 90), pygame.Rect(width / 2 - 200, height / 2 - 100, 400, 200))

            if width / 2 - 100 <= mouse[0] <= width / 2 - 100 + 200 and height / 2 <= mouse[1] <= height / 2 + 30:
                pygame.draw.rect(screen, color_light, pygame.Rect(width/2 - 100, height / 2, 200, 30))
            else:
                pygame.draw.rect(screen, color_dark, pygame.Rect(width/2 - 100, height / 2, 200, 30))

            if width / 2 - 100 <= mouse[0] <= width / 2 - 100 + 200 and height / 2 + 50 <= mouse[1] <= height / 2 + 50 + 30:
                pygame.draw.rect(screen, color_light, pygame.Rect(width/2 - 100, height / 2 + 50, 200, 30))
            else:
                pygame.draw.rect(screen, color_dark, pygame.Rect(width/2 - 100, height / 2 + 50, 200, 30))

            screen.blit(koniec, (width / 2 - koniec.get_width() / 2, height / 2 - 50))
            screen.blit(gra, (width / 2 - gra.get_width() / 2, height / 2 + 2))
            screen.blit(wyjscie, (width / 2 - wyjscie.get_width() / 2, height / 2 + 52))

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    sys.exit(0)
                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                    if width / 2 - 100 <= mouse[0] <= width / 2 - 100 + 200 and height / 2 <= mouse[1] <= height / 2 + 30:
                        self.start()
                    elif width / 2 - 100 <= mouse[0] <= width / 2 - 100 + 200 and height / 2 + 50 <= mouse[1] <= height / 2 + 50 + 30:
                        sys.exit(0)

            pygame.display.update()

        sys.exit(0)

    def start(self):
        screen = pygame.display.set_mode((600, 400))
        width = screen.get_width()
        height = screen.get_height()

        white = (255, 255, 255)
        color_light = (130, 130, 130)
        color_dark = (100, 100, 100)
        font1 = pygame.font.SysFont('Arial', 24)
        bigfont = pygame.font.SysFont('Arial black', 44)
        smallfont = pygame.font.SysFont('Arial', 16)

        nazwa = bigfont.render('The Organisms 2.0', True, white)
        autor = smallfont.render('by Jakub Link 184469', True, white)
        nowagra = font1.render('Nowa Gra', True, white)
        wczytaj = font1.render('Wczytaj świat z pliku', True, white)

        gra = False
        while not gra:
            screen.fill((150, 150, 150))
            mouse = pygame.mouse.get_pos()

            if width / 2 - 100 <= mouse[0] <= width / 2 - 100 + 200 and 200 <= mouse[1] <= 200 + 30:
                pygame.draw.rect(screen, color_light, pygame.Rect(width/2 - 100, 200, 200, 30))
            else:
                pygame.draw.rect(screen, color_dark, pygame.Rect(width/2 - 100, 200, 200, 30))

            if width / 2 - 100 <= mouse[0] <= width / 2 - 100 + 200 and 300 <= mouse[1] <= 300 + 30:
                pygame.draw.rect(screen, color_light, pygame.Rect(width/2 - 100, 300, 200, 30))
            else:
                pygame.draw.rect(screen, color_dark, pygame.Rect(width/2 - 100, 300, 200, 30))

            screen.blit(nazwa, (width / 2 - nazwa.get_width() / 2, 80))
            screen.blit(autor, (width / 2 + 50, 80 + nazwa.get_height()))
            screen.blit(nowagra, (width / 2 - 100 + (200 - nowagra.get_width()) / 2, 200))
            screen.blit(wczytaj, (width / 2 - 100 + (200 - wczytaj.get_width()) / 2, 300))

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    sys.exit(0)
                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                    if width / 2 - 100 <= mouse[0] <= width / 2 - 100 + 200 and 200 <= mouse[1] <= 200 + 30:
                        self.__generuj()
                        gra = True

                    elif width / 2 - 100 <= mouse[0] <= width / 2 - 100 + 200 and 300 <= mouse[1] <= 300 + 30:
                        sciezka = ''
                        zatwierdzone = False
                        komunikat = font1.render("Podaj ścieżkę pliku: ", True, white)
                        while not zatwierdzone:
                            for ev in pygame.event.get():
                                if ev.type == pygame.QUIT:
                                    sys.exit(0)
                                if ev.type == pygame.KEYDOWN:
                                    if ev.key == pygame.K_BACKSPACE:
                                        sciezka = sciezka[:-1]
                                    elif ev.key == pygame.K_RETURN:
                                        if len(sciezka) > 0:
                                            zatwierdzone = True
                                    else:
                                        sciezka += ev.unicode

                            screen.fill((100, 100, 100))

                            screen.blit(komunikat, (40, 100))
                            wart = font1.render(sciezka, True, white)
                            screen.blit(wart, (220, 100))
                            pygame.display.update()

                        while not os.path.exists(sciezka):
                            sciezka = ''
                            zatwierdzone = False
                            komunikat = font1.render("Podaj poprawną ścieżkę pliku: ", True, white)
                            while not zatwierdzone:
                                for ev in pygame.event.get():
                                    if ev.type == pygame.QUIT:
                                        sys.exit(0)
                                    if ev.type == pygame.KEYDOWN:
                                        if ev.key == pygame.K_BACKSPACE:
                                            sciezka = sciezka[:-1]
                                        elif ev.key == pygame.K_RETURN:
                                            if len(sciezka) > 0:
                                                zatwierdzone = True
                                        else:
                                            sciezka += ev.unicode

                                screen.fill((100, 100, 100))

                                screen.blit(komunikat, (20, 100))
                                wart = font1.render(sciezka, True, white)
                                screen.blit(wart, (290, 100))
                                pygame.display.update()

                        self.__wczytaj(sciezka)
                        gra = True

            pygame.display.update()

        self.__graj()
