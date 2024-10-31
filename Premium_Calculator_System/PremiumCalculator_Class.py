from Customer_Class import Customer
from HealthInsurance_Class import HealthInsurance, MedicalCondition
from AutoInsurance_Class import AutoInsurance
from LifeInsurance_Class import LifeInsurance

class PremiumCalculator:
    def generate_quote(self, customer: Customer, policy_type: str, **kwargs) -> float:
        if policy_type == 'Health':
            # Use 'medical_condition' instead of 'has_medical_conditions'
            policy = HealthInsurance(kwargs['base_premium'], customer.age, kwargs['medical_condition'])
        
        elif policy_type == 'Auto':
            policy = AutoInsurance(kwargs['base_premium'], customer.age, kwargs['driving_record'], kwargs['vehicle_type'])
        
        elif policy_type == 'Life':
            policy = LifeInsurance(kwargs['base_premium'], customer.age, kwargs['coverage_amount'])
        
        else:
            raise ValueError("Unknown policy type")

        customer.add_policy(policy)
        return policy.calculate_premium()
