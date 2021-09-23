from ihouse_builder import IHouseBuilder
from house import House


class CheapHouseBuilder(IHouseBuilder):
    def new_house(self):
        self._house = House()

    def build_wall(self):
        self._house.wall = "drewanie"

    def build_door(self):
        self._house.door = "drewniane"

    def build_window(self):
        self._house.window = "standard"

    def build_floor(self):
        self._house.floor = "pcv"

    def build_garden(self):
        self._house.garden = "mały"

    def build_garage(self):
        self._house.garage = None

    def build_swimming_pool(self):
        self._house.swimming_pool = None

    def get_house(self):
        return self._house
