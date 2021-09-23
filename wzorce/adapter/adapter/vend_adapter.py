from iadapter import IAdapter


class VendAdapter(IAdapter):
    @property
    def name(self):
        return self._adaptee.name

    @property
    def address(self):
        return f"{self._adaptee.street} {self._adaptee.number}"
