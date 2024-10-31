from Policy_Class import Policy
from enum import Enum

class MedicalCondition(Enum):
    NONE = 0
    DIABETES = 1
    HEART_DISEASE = 2
    CANCER = 3

class HealthInsurance(Policy):
    def __init__(self, base_premium: float, age: int, medical_condition: MedicalCondition = MedicalCondition.NONE):
        super().__init__('Health', base_premium)
        self.age = age
        self.medical_condition = medical_condition

    def calculate_premium(self) -> float:
        premium = self.base_premium + (self.age * 5)
        # Add premium based on medical condition severity
        if self.medical_condition == MedicalCondition.DIABETES:
            premium += 100
        elif self.medical_condition == MedicalCondition.HEART_DISEASE:
            premium += 200
        elif self.medical_condition == MedicalCondition.CANCER:
            premium += 300
        return premium
