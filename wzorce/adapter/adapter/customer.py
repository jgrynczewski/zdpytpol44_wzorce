class Customer:
    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    @property
    def name(self):
        return self.__name

    @property
    def address(self):
        return self.__address
