import string
import random


class VehicleRegistry:
    def __generate_vehicle_id(self):
        return "".join(random.choices(string.ascii_uppercase, k=12))

    def __generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}" \
               f"-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def get_vehicle_license(self):
        vehicle_id = self.__generate_vehicle_id()
        vehicle_license = self.__generate_vehicle_license(vehicle_id)
        return vehicle_license


class VehicleInfo:
    def __init__(self, brand):
        self.brand = brand

    def __get_price(self):
        catalogue_price = 0
        if self.brand == 'Tesla Model 3':
           catalogue_price = 100000
        elif self.brand == 'Volkswagen ID3':
            catalogue_price = 60000
        elif self.brand == 'BMW 5':
            catalogue_price = 75000

        return catalogue_price

    def __get_tax(self):
        tax_percentage = 0.05
        if self.brand == "Tesla Model 3" or self.brand == "Volkswagen ID3":
            tax_percentage = 0.02

        return tax_percentage

    def get_payable_tax(self):
        return self.__get_price() * self.__get_tax()


class Application:
    def register_vehicle(self, brand: string):
        # create a register instance
        registry = VehicleRegistry()
        license_plate = registry.get_vehicle_license()

        info = VehicleInfo(brand)
        payable_tax = info.get_payable_tax()

        # print out the vehicle registration information
        print("Registration complete. Vehicle information:")
        print(f"Brand: {brand}")
        print(f"License plate: {license_plate}")
        print(f"Payable tax: {payable_tax}")

app = Application()
app.register_vehicle("BMW 5")
