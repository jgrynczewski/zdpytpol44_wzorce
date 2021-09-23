from mock_customer import MOCKCUSTOMER
from mock_vendor import MOCKVENDOR


def main():
    for cust in MOCKCUSTOMER+MOCKVENDOR:
        print(f"Name: {cust.name}; Adres: {cust.address}")


if __name__ == '__main__':
    main()
