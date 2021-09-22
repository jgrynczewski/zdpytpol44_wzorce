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

# Nie łamiemy OCP
class Filter:
    def filter(self, products, spec):
        for item in products:
            if spec.is_satisfied(item):
                yield item


class ColorSpecification:
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification:
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


new_filter = Filter()
green_spec = ColorSpecification("GREEN")

print("New filter. Only green products:")
for item in new_filter.filter(products, green_spec):
    print(f"\t{item.name} is green.")

large_spec = SizeSpecification("LARGE")
print("New filter. Only large products:")
for item in new_filter.filter(products, large_spec):
    print(f"\t{item.name} is large.")
