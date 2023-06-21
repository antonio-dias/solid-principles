from product import Product
from inHouseProduct import InHouseProduct

class PricingUtils:

    def __init__(self):
        p1 = Product()
        p2 = Product()
        p3 = InHouseProduct()

        productList = []
        productList.append(p1)
        productList.append(p2)
        productList.append(p3)

        for product in productList:
            print(product.getDiscount())

PricingUtils()