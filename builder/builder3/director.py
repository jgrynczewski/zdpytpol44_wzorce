from ihouse_builder import IHouseBuilder


class Director:
    def __init__(self, builder: IHouseBuilder):
        self._builder = builder

    def build_house(self):
        self._builder.new_house()
        self._builder.build_wall()
        self._builder.build_door()
        self._builder.build_window()
        self._builder.build_floor()
        self._builder.build_garden()
        self._builder.build_garage()
        self._builder.build_swimming_pool()

    def get_house(self):
        return self._builder.get_house()