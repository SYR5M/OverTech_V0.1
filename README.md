Premium_Calculator_System
Premium_Calculator_System is a Python application that calculates insurance premium quotes for different types of insurance policies, including health, auto, and life insurance. This project leverages Object-Oriented Programming principles for flexibility, scalability, and maintainability.

Features
Flexible Premium Calculation: Unique formulas for each insurance type based on customer-specific factors (e.g., age, medical conditions, driving record).
Modular Design: Built with an Object-Oriented structure, making it easy to expand by adding new types of insurance or risk factors.
Comprehensive Testing: Includes unit tests to verify accurate premium calculations across various scenarios.
UML Class Diagram: A diagram illustrating the relationships between classes in the system.
Project Structure
Customer_Class.py: Manages customer information, including ID, name, age, and insurance policies.
Policy_Class.py: Base class for all insurance policies, with subclasses for each policy type.
HealthInsurance_Class.py, AutoInsurance_Class.py, LifeInsurance_Class.py: Specialized classes for each insurance type with custom premium calculation methods.
PremiumCalculator_Class.py: Main class that generates premium quotes based on customer and policy details.
Main.py: Main program to demonstrate the system’s functionality.
Unit_Tests.py: Contains unit tests to verify that premium calculations are accurate.
uml_diagram_updated.png: UML Class Diagram illustrating class relationships.
License
This project is open-source and available under the MIT License.
