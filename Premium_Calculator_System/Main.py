from Customer_Class import Customer
from HealthInsurance_Class import HealthInsurance, MedicalCondition
from AutoInsurance_Class import AutoInsurance
from LifeInsurance_Class import LifeInsurance
from PremiumCalculator_Class import PremiumCalculator

def main():
    # Create a young customer for auto insurance
    young_driver = Customer(101, "Alice", 22, "456 Oak Street")
    calculator = PremiumCalculator()
    auto_premium = calculator.generate_quote(
        young_driver, 'Auto', base_premium=150, driving_record='clean', vehicle_type='Sedan'
    )
    print(f"Auto Insurance Premium for young driver: ${auto_premium:.2f}")

    # Create a customer for high coverage life insurance
    life_insured = Customer(102, "Bob", 40, "789 Pine Road")
    life_premium = calculator.generate_quote(
        life_insured, 'Life', base_premium=100, coverage_amount=1000000
    )
    print(f"Life Insurance Premium with high coverage: ${life_premium:.2f}")

    # Create a senior customer with health conditions for health insurance
    senior_customer = Customer(103, "Carol", 65, "321 Maple Ave")
    health_premium = calculator.generate_quote(
        senior_customer, 'Health', base_premium=200, medical_condition=MedicalCondition.HEART_DISEASE
    )
    print(f"Health Insurance Premium for senior with medical conditions: ${health_premium:.2f}")

if __name__ == "__main__":
    main()
