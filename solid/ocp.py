# Open-close Principle

# Łamiemy OCP
class Animal:
    def __init__(self, name):
        self.name = name


def sound_animal(animals: list):
    for animal in animals:
        if animal.name == 'Lion':
            print('roar')
        elif animal.name == 'Mouse':
            print('squek')
        elif animal.name == 'Snake':
            print('hiss')


animals = [
    Animal('Lion'),
    Animal('Mouse'),
    Animal('Snake')
]
sound_animal(animals)


# Nie łamiemy OCP
import abc


class Animal(abc.ABC):
    @abc.abstractmethod
    def make_sound(self):
        pass


class Lion(Animal):
    def make_sound(self):
        return 'roar'


class Mouse(Animal):
    def make_sound(self):
        return 'squek'


class Snake(Animal):
    def make_sound(self):
        return 'hiss'


def sound_animal(animals):
    for animal in animals:
        print(animal.make_sound())


animals = [
    Lion(),
    Mouse(),
    Snake()
]

print("=========")
sound_animal(animals)
