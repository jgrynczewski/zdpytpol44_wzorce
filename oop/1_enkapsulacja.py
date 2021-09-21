# hermetyzacja, kapsułkowanie

class Account:
    def __init__(self, balance):
        self.balance = balance

    def __str__(self):
        return f"Stan konta: {self.balance}$"


a = Account(100)
a.balance = 250
a.balance = -350
a.balance = "abc"
print(a)


class Account:
    def __init__(self, balance):
        self.balance = balance

    # setter (aka mutator)
    def set_balance(self, value):
        if type(value) not in [int, float] or value < 0:
            print("Niepoprawna wartość!")
        else:
            self.balance = value

    # getter (aka accessor)
    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Stan konta: {self.balance}$"


print("=======================")
a = Account(100)
print(a.get_balance())
a.set_balance("abc")
a.set_balance("-200")
a.balance = -200
print(a.get_balance())
print(a)

# Modyfikatory dostępu (access modifiers) - składowe publiczne, chronione i prywatne

class Account:
    def __init__(self, balance):
        self.__balance = balance

    # setter (aka mutator)
    def set_balance(self, value):
        if type(value) not in [int, float] or value < 0:
            print("Niepoprawna wartość!")
        else:
            self.__balance = value

    # getter (aka accessor)
    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Stan konta: {self.__balance}$"


print("++++++++++++++++++++++++++++++++++++++")
a = Account(100)
print(a.get_balance())
a.set_balance("abc")
a.set_balance("-200")
a.set_balance(a.get_balance() + 2*(a.get_balance())**2) # to nie wygląda dobrze
print(a.get_balance())
print(a)


# Property
class Account:
    def __init__(self, balance):
        self.__balance = balance

    # setter (aka mutator)
    def set_balance(self, value):
        if type(value) not in [int, float] or value < 0:
            print("Niepoprawna wartość!")
        else:
            self.__balance = value

    # getter (aka accessor)
    def get_balance(self):
        return self.__balance

    balance = property(get_balance, set_balance)

    def __str__(self):
        return f"Stan konta: {self.__balance}$"


print("---------------------------------------------")
a = Account(100)
print(a.balance)
a.balance = "abc"
a.balance = -200
a.balance = a.balance + 2*(a.balance)**2 # to wygląda lepiej
print(a.balance)
print(a)

# Alternatywna notacja z użyciem dekoratorów
class Account:
    def __init__(self, balance):
        self.__balance = balance

    # getter (aka accessor)
    @property
    def balance(self):
        return self.__balance

    # setter (aka mutator)
    @balance.setter
    def balance(self, value):
        if type(value) not in [int, float] or value < 0:
            print("Niepoprawna wartość!")
        else:
            self.__balance = value

    def __str__(self):
        return f"Stan konta: {self.__balance}$"


print("###############################################")
a = Account(100)
print(a.balance)
a.balance = "abc"
a.balance = -200
a.balance = a.balance + 2*(a.balance)**2 # to wygląda lepiej
print(a.balance)
print(a)

# Czasamie dodaje się też deleter