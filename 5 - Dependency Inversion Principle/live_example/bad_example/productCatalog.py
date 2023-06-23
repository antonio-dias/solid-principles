from sqlProductRepository import SQLProductRepository

class ProductCatalog:

    def listAllProduct(self):
        sqlProductRepository = SQLProductRepository()
        sqlProductRepository.getAllProductNames()
        # List all products here