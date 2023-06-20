from customerProfile import CustomerProfile

class InsurancePremiumDiscountCalculator:

    def calculatePremiumDiscountPercent(self, customer: CustomerProfile):
        if customer.isLoyalCustomer():
            return 20
        return 0

