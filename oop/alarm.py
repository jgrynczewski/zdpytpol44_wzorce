class Alarm:
    def __init__(self, model):
        self.model = model
        self.status = 'off'

    def turn_on(self):
        self.status = 'on'

    def turn_off(self):
        self.status = 'off'


class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Nazywam się {self.name}")


class Owner(Person):
    def turn_on_alarm(self, alarm):
        alarm.turn_on()


class Thief(Person):
    pass


my_alarm = Alarm('XF32')
my_alarm2 = Alarm('CD44')
# print(my_alarm.status)
# my_alarm.turn_on()
# print(my_alarm.status)

adam = Owner('Adam')
adam.turn_on_alarm(my_alarm)
adam.turn_on_alarm(my_alarm2)

print(f"Status alarmu {my_alarm.status}")

print("=============================")

bob = Thief('Bob')

adam.introduce()
bob.introduce()