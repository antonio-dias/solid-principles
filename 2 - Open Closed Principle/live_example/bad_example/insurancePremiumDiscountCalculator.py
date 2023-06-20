from vehicleInsuranceCustomerProfile import VehicleInsuranceCustomerProfile
from healthInsuranceCustomerProfile import HealthInsuranceCustomerProfile

class InsurancePremiumDiscountCalculator:

    def calculatePremiumDiscountPercent(self, customer: HealthInsuranceCustomerProfile):
        if customer.isLoyalCustomer():
            return 20
        return 0

    def calculatePremiumDiscountPercent(self, customer: VehicleInsuranceCustomerProfile):
        if customer.isLoyalCustomer():
            return 20
        return 0

