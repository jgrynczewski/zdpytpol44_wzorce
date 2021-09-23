from standard_house_builder import StandardHouseBuilder
from cheap_house_builder import CheapHouseBuilder

builder = StandardHouseBuilder()
builder.new_house()
builder.build_wall()
builder.build_door()
builder.build_window()
builder.build_floor()
builder.build_garden()
builder.build_garage()
builder.build_swimming_pool()
standard_house = builder.get_house()

builder = CheapHouseBuilder()
builder.new_house()
builder.build_wall()
builder.build_door()
builder.build_window()
builder.build_floor()
builder.build_garden()
builder.build_garage()
builder.build_swimming_pool()
cheap_house = builder.get_house()

standard_house.display()
print("================")
cheap_house.display()