from random import Random
from customerProfile import CustomerProfile

class HealthInsuranceCustomerProfile(CustomerProfile):

    def isLoyalCustomer(self):
        return Random.randbytes()