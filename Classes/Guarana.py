from Classes.Roslina import Roslina


class Guarana(Roslina):
    def __init__(self, X, Y, swiat, wiek):
        Roslina.__init__(self, 'Guarana', X, Y, swiat, wiek, 0)

    def kolizja(self, napastnik):
        Roslina.kolizja(self, napastnik)
        info = '  zwiększenie siły z ' + str(napastnik.get_sila()) + ' do '

        self._swiat.get_organizmy().find_element(self._X, self._Y).set_sila(self._swiat.get_organizmy().find_element(self._X, self._Y).get_sila() + 3)
        self._swiat.get_mapa()[self._X][self._Y].set_sila(self._swiat.get_organizmy().find_element(self._X, self._Y).get_sila())

        info += str(self._swiat.get_organizmy().find_element(self._X, self._Y).get_sila())
        self._swiat.dodaj_info(info)

    def _rozmnazanie(self, x, y):
        self._swiat.dodaj_info('Guarana rozprzestrzenia się.')
        sadzonka = Guarana(x, y, self._swiat, 0)
        self._swiat.get_mapa()[x][y] = sadzonka
        self._swiat.get_nowo_narodzone().add(sadzonka)

    def rysowanie(self):
        return (230, 0, 230)
