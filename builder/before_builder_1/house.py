class House:
    def __init__(self, wall, door, window, floor, garden, garage, swimming_pool):
        self.wall = self.build_wall() if wall else None
        self.door = self.build_door() if door else None
        self.window = self.build_window() if window else None
        self.floor = self.build_floor() if floor else None
        self.garden = self.build_garden() if garden else None
        self.garage = self.build_garage() if garage else None
        self.swimming_pool = self.build_swimming_pool() if swimming_pool else None

    def build_wall(self):
        return "murowane"

    def build_door(self):
        return "antywłamaniowe"

    def build_window(self):
        return "kulodporne"

    def build_floor(self):
        return "panele"

    def build_garden(self):
        return "Duży"

    def build_garage(self):
        return "Podziemny"

    def build_swimming_pool(self):
        return "Kryty"


    def display(self):
        print(f"Ściany: {self.wall}")
        print(f"Drzwi: {self.door}")
        print(f"Okna: {self.window}")
        print(f"Podłoga: {self.floor}")
        print(f"Ogród: {self.garden}")
        print(f"Garaż: {self.garage}")
        print(f"Basen: {self.swimming_pool}")
