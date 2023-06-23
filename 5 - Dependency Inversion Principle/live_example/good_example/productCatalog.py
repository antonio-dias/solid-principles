from productFactory import ProductFactory

class ProductCatalog:

    def listAllProduct(self):
        productRepository = ProductFactory().create()
        productRepository.getAllProductNames()
        # List all products here