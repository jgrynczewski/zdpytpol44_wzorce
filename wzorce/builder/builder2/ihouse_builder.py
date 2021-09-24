import abc


class IHouseBuilder(abc.ABC):
    @abc.abstractmethod
    def new_house(self):
        pass

    @abc.abstractmethod
    def build_wall(self):
        pass

    @abc.abstractmethod
    def build_door(self):
        pass

    @abc.abstractmethod
    def build_window(self):
        pass

    @abc.abstractmethod
    def build_floor(self):
        pass

    @abc.abstractmethod
    def build_garden(self):
        pass

    @abc.abstractmethod
    def build_garage(self):
        pass

    @abc.abstractmethod
    def build_swimming_pool(self):
        pass

    @abc.abstractmethod
    def get_house(self):
        pass
