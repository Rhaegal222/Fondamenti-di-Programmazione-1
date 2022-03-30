class CashRegister:

    def __init__(self):
        self._itemCount = 0
        self._totalPrice = 0

    def addItem(self, price):
        self._itemCount += 1
        self._totalPrice += price

    def addItems(self, quantity, price):
        for i in range(quantity):
            self.addItem(price)

    def getTotal(self):
        return self._totalPrice

    def getCount(self):
        return self._itemCount

    def clear(self):
        self._itemCount = 0
        self._totalPrice = 0

register1 = CashRegister()

register1.addItems(6, 0.95)

print('Numero di articoli:', register1.getCount())
print('Totale:', register1.getTotal())