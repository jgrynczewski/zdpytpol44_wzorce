# DIP - Dependency Inversion Principle
# Nie łamimy DIP (i nie łamimy OCP)
import abc


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.size = size
        self.color = color


class ISpecification(abc.ABC):
    @abc.abstractmethod
    def is_satisfied(self, item):
        pass


class ColorSpecification(ISpecification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(ISpecification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class Filter:
    def filter(self, products, spec: ISpecification):
        for item in products:
            if spec.is_satisfied(item):
                yield item


apple = Product("Apple", "GREEN", 'SMALL')
tree = Product("Tree", "GREEN", 'LARGE')
house = Product("House", "BLUE", 'LARGE')

products = [apple, tree, house]
new_filter = Filter()
green_spec = ColorSpecification("GREEN")

print("New filter. Only green products:")
for item in new_filter.filter(products, green_spec):
    print(f"\t{item.name} is green.")

large_spec = SizeSpecification("LARGE")
print("New filter. Only large products:")
for item in new_filter.filter(products, large_spec):
    print(f"\t{item.name} is large.")
