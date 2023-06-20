import abc

class CustomerProfile:

    @abc.abstractmethod
    def isLoyalCustomer(self):
        return