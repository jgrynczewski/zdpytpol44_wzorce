# OCP

# Łamiemy OCP
class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.size = size
        self.color = color


class ProductFilter:
    def filter_by_color(self, products, color):
        for item in products:
            if item.color == color:
                yield item

    def filter_by_size(self, products, size):
        for item in products:
            if item.size == size:
                yield item

    def filter_by_color_and_size(self, products, color, size):
        for item in products:
            if item.size == size and item.color == color:
                yield item


apple = Product("Apple", "GREEN", 'SMALL')
tree = Product("Tree", "GREEN", 'LARGE')
house = Product("House", "BLUE", 'LARGE')

products = [apple, tree, house]

pf = ProductFilter()
print("Only green products:")
for item in pf.filter_by_color(products, "GREEN"):
    print(f"\t{item.name} is green.")

print("Only large products:")
for item in pf.filter_by_size(products, "LARGE"):
    print(f"\t{item.name} is large.")

print("Only large, green products:")
for item in pf.filter_by_color_and_size(products, "GREEN", "LARGE"):
    print(f"\t{item.name} is green and large.")

