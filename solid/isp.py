# ISP - Interface Seperation Principle
import abc

# Łamiemy ISP
class IMachine(abc.ABC):
    @abc.abstractmethod
    def print(self, document):
        raise NotImplemented

    @abc.abstractmethod
    def scan(self, document):
        raise NotImplemented

    @abc.abstractmethod
    def fax(self, document):
        raise NotImplemented


class MulitfunctionalPrinter(IMachine):
    def print(self, document):
        print("Drukuję")

    def scan(self, document):
        print("Skanuję")

    def fax(self, document):
        print("Faksuję")


class OldFashionedPrinter(IMachine):
    def print(self, document):
        print("Drukuję")

    def scan(self, document):
        """Not supported"""
        raise NotImplemented("Printer cannot scan")

    def fax(self, documenet):
        """Not supported"""
        raise NotImplemented("Printer cannot fax")


# Client
my_printer = OldFashionedPrinter()
my_printer.fax('abc')

# Nie łamiemy ISP
class IPrinter(abc.ABC):
    @abc.abstractmethod
    def print(self, document):
        pass


class IScanner(abc.ABC):
    @abc.abstractmethod
    def scan(self, document):
        pass


class IFax(abc.ABC):
    @abc.abstractmethod
    def fax(self, document):
        pass


class OldFashionedPrinter(IPrinter):
    def print(self, document):
        print("Drukuję")


class PhotoCopier(IPrinter, IScanner):
    def print(self, document):
        print("Drukuję")

    def scan(self, document):
        print("Skaner")

class IMultifunctionalMachine(IPrinter, IScanner, IFax):
