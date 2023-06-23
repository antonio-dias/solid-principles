from sqlProductRepository import SQLProductRepository


class ProductFactory:

    def create(self):
        return SQLProductRepository()
