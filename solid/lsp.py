# LSP

import abc


class Animal(abc.ABC):
    @property
    @abc.abstractmethod
    def num_legs(self):
        pass


class Lion(Animal):
    def __init__(self):
        self.__num_legs = 4

    def num_legs(self):
        return self.__num_legs


class Penquin(Animal):
    def __init__(self):
        self.__num_legs = 2

    def num_legs(self):
        return self.__num_legs


class Snake(Animal):
    def __init__(self):
        self.__num_legs = 0

    def num_legs(self):
        return self.__num_legs


class Herd:
    def __init__(self, animal: Animal, num_legs):
        self.animal = animal
        self.num_legs = num_legs # liczba nóg w stadzie

    def count_members(self):
        return int(self.num_legs / self.animal.num_legs)


# Client
penquin = Penquin()
lion = Lion()
snake = Snake()

herds = [
    Herd(lion, 32),
    Herd(penquin, 14),
    Herd(snake, 15)
]

for herd in herds:
    print(f"W stadzie jest {herd.count_members()}")