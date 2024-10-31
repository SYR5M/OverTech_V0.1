class Customer:
    def __init__(self, customer_id: int, name: str, age: int, address: str):
        self.customer_id = customer_id
        self.name = name
        self.age = age
        self.address = address
        self.past_policies = []

    def add_policy(self, policy):
        self.past_policies.append(policy)

    def get_info(self) -> str:
        return f"ID: {self.customer_id}, Name: {self.name}, Age: {self.age}, Address: {self.address}"
