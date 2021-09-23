from house import House


class HouseBuilder:
    def new_house(self):
        self._house = House()

    def build_wall(self):
        self._house.wall = "murowane"

    def build_door(self):
        self._house.door = "antywłamaniowe"

    def build_window(self):
        self._house.window = "kulodporne"

    def build_floor(self):
        self._house.floor = "panele"

    def build_garden(self):
        self._house.garden = "Duży"

    def build_garage(self):
        self._house.garage = None

    def build_swimming_pool(self):
        self._house.swimming_pool = "Kryty"

    def get_house(self):
        return self._house
