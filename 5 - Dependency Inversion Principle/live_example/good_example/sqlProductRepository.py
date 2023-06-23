from productRepository import ProductRepository


class SQLProductRepository(ProductRepository):

    def getAllProductNames(self):
        return ["soap", "toothpaste"]