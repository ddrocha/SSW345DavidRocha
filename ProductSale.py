# needed for forward reference of Sale in Product,
# since Sale is not yet defined.
from __future__ import annotations
from typing import List

# forward reference used for class Sale
class Product:
    __lastSale: Sale = None
    __inventory: int = 0

    def __init__(self, sale: Sale, inventory: int):
        self.__lastSale = sale
        self.__inventory = inventory

    def setLastSale(self, lastSale: Sale):
        self.__lastSale = lastSale

    @property
    def getLastSale(self) -> Sale:
        return self.__lastSale

    @property
    def getInventory(self) -> int:
        return self.__inventory

    def reduceInventory(self, quantity: int):
        if quantity > self.__inventory:
            raise ValueError("Not enough inventory to fulfill sale.")
        self.__inventory -= quantity

    def __getitem__(self, item):
        return self

# no forward reference needed since Product is defined
class Sale:
    __saleTimes = 0
    __productSold: List[Product] = None
    __saleNumber: int = 0

    def __init__(self, product: List[Product], quantities: List[int]):
        Sale.__saleTimes += 1
        self.__product = product
        self.__saleNumber = Sale.__saleTimes

        for index, product in enumerate(product):
            if index < len(quantities):
                product.reduceInventory(quantities[index])
            product.setLastSale(self)

    def setProductsSold(self, productSold: List[Product]):
        self.__productSold = productSold

    @property
    def getSaleNumber(self) -> int:
        return self.__saleNumber


productOne = Product(sale=None, inventory=10)
productTwo = Product(sale=None, inventory=15)

saleOne = Sale([productOne, productTwo], [2, 3])
saleTwo = Sale([productOne], [1])
saleThree = Sale([productTwo], [5])

print(f"Product 1: Last sale number: {productOne.getLastSale.getSaleNumber}, Remaining inventory: {productOne.getInventory}")
print(f"Product 2: Last sale number: {productTwo.getLastSale.getSaleNumber}, Remaining inventory: {productTwo.getInventory}")
