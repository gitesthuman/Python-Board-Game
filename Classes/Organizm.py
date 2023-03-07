class Organizm:
    def __init__(self, nazwa, X, Y, swiat, wiek, sila, inincjatywa):
        self._nazwa = nazwa
        self._X = X
        self._Y = Y
        self._swiat = swiat
        self._wiek = wiek
        self._sila = sila
        self._inicjatywa = inincjatywa

    def akcja(self):
        pass

    def kolizja(self):
        pass

    def rysowanie(self):
        pass

    def get_nazwa(self):
        return self._nazwa

    def get_X(self):
        return self._X

    def set_X(self, X):
        self._X = X

    def get_Y(self):
        return self._Y

    def set_Y(self, Y):
        self._Y = Y

    def get_wiek(self):
        return self._wiek

    def set_wiek(self, wiek):
        self._wiek = wiek

    def get_sila(self):
        return self._sila

    def set_sila(self, sila):
        self._sila = sila

    def get_inicjatywa(self):
        return self._inicjatywa

    def _losuj_pole(self, cords):
        pass

    def _rozmnazanie(self, x, y):
        pass