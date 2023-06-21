from product import Product

class InHouseProduct(Product):

    def __init__(self):
        super().__init__()

    def applyExtraDiscount(self):
        self.discount = self.discount * 1.5