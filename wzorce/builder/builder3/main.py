from standard_house_builder import StandardHouseBuilder
from cheap_house_builder import CheapHouseBuilder
from director import Director

standard_builder = StandardHouseBuilder()
director = Director(standard_builder)
director.build_house()
standard_house = director.get_house()

cheap_builder = CheapHouseBuilder()
director = Director(cheap_builder)
director.build_house()
cheap_house = director.get_house()

standard_house.display()
print("================")
cheap_house.display()