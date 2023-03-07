class Lista:
    def __init__(self):
        self.__tab = []
        self.__current = 0

    def add(self, organizm):
        for i in range(0, len(self.__tab)):
            if self.__tab[i].get_inicjatywa() < organizm.get_inicjatywa():
                self.__tab.insert(i, organizm)
                return
        self.__tab.insert(len(self.__tab), organizm)

    def find_element(self, x, y):
        for i in range(0, len(self.__tab)):
            if self.__tab[i].get_X() == x and self.__tab[i].get_Y() == y:
                return self.__tab[i]
        return None

    def del_element(self, x, y):
        for i in range(0, len(self.__tab)):
            if self.__tab[i].get_X() == x and self.__tab[i].get_Y() == y:
                self.__tab.pop(i)
                if self.__current == len(self.__tab):
                    self.__current = 0
                break

    def get_size(self):
        return len(self.__tab)

    def get_current(self):
        return self.__tab[self.__current % len(self.__tab)]

    def get_end(self):
        return self.__tab[len(self.__tab) - 1]

    def next(self):
        self.__current = (self.__current + 1) % len(self.__tab)

    def __del__(self):
        del self.__tab