import abc

class CustomerProfile(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def isLoyalCustomer(self):
        return