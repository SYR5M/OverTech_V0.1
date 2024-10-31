class Policy:
    def __init__(self, policy_type: str, base_premium: float):
        self.policy_type = policy_type
        self.base_premium = base_premium

    def calculate_premium(self) -> float:
        raise NotImplementedError("This method should be overridden by subclasses")
