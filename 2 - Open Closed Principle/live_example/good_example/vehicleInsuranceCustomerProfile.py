from random import Random
from customerProfile import CustomerProfile

class VehicleInsuranceCustomerProfile(CustomerProfile):

    def isLoyalCustomer(self):
        return Random.randbytes()