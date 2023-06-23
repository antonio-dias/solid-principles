import abc


class ProductRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def getAllProductNames(self):
        return