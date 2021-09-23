from house_builder import HouseBuilder

builder = HouseBuilder()
builder.new_house()
builder.build_wall()
builder.build_door()
builder.build_window()
builder.build_floor()
builder.build_garden()
builder.build_garage()
builder.build_swimming_pool()
my_house = builder.get_house()

my_house.display()