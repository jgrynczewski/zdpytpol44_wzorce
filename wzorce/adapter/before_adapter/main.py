from mock_customer import MOCKCUSTOMER
from mock_vendor import MOCKVENDOR

TYPE = 'sds'


def main():
    if TYPE == 'client':
        for cust in MOCKCUSTOMER:
            print(f"Name: {cust.name}; Adres: {cust.address}")
    elif TYPE == 'vendor':
        for vendor in MOCKVENDOR:
            print(f"Name: {vendor.name}; Adres: {vendor.street} {vendor.number}")
    else:
        raise ValueError(f"Incorret type {TYPE}")


if __name__ == '__main__':
    main()
