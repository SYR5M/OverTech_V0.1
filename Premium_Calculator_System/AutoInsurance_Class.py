from Policy_Class import Policy

class AutoInsurance(Policy):
    def __init__(self, base_premium: float, age: int, driving_record: str, vehicle_type: str):
        super().__init__('Auto', base_premium)
        self.age = age
        self.driving_record = driving_record
        self.vehicle_type = vehicle_type

    def calculate_premium(self) -> float:
        premium = self.base_premium + (self.age * 3)
        if self.driving_record == 'bad':
            premium += 200
        return premium
