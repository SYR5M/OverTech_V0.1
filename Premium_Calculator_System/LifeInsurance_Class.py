from Policy_Class import Policy

class LifeInsurance(Policy):
    def __init__(self, base_premium: float, age: int, coverage_amount: float):
        super().__init__('Life', base_premium)
        self.age = age
        self.coverage_amount = coverage_amount

    def calculate_premium(self) -> float:
        premium = self.base_premium + (self.age * 2) + (self.coverage_amount * 0.001)
        return premium
