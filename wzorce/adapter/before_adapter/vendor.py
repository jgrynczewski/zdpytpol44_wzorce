class Vendor:
    def __init__(self, name, street, number):
        self.__name = name
        self.__street = street
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def street(self):
        return self.__street

    @property
    def number(self):
        return self.__number