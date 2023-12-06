"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract_type, salary=0, hours_worked=1, hourly_rate=0, bonus=0, contracts=1, commission_rate=0):
        self.name = name
        self.contract_type = contract_type
        self.salary = salary
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.bonus = bonus
        self.contracts = contracts
        self.commission_rate = commission_rate

    def get_pay(self):
        if self.contract_type == 'salary':
            contract_pay = self.salary
        elif self.contract_type == 'hourly':
            contract_pay = self.hours_worked * self.hourly_rate
        else:
            raise ValueError("Invalid contract type")

        commission = 0
        if self.bonus:
            commission += self.bonus
        if self.contracts and self.commission_rate:
            commission += self.contracts * self.commission_rate

        total_pay = contract_pay + commission
        return total_pay

    def __str__(self):
        if self.contract_type == 'salary':
            explanation = f"{self.name} works on a monthly salary of {self.salary}"
        elif self.contract_type == 'hourly':
            explanation = f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_rate}/hour"
        else:
            raise ValueError("Invalid contract type")

        commission_explanation = ""
        if self.bonus!=0:
            commission_explanation += f" and receives a bonus commission of {self.bonus}"
        if self.contracts and self.commission_rate:
            commission_explanation += f" and receives a commission for {self.contracts} contract(s) at {self.commission_rate}/contract"

        total_explanation = f". Their total pay is {self.get_pay()}."

        return explanation + commission_explanation + total_explanation

# Billie
billie = Employee('Billie', 'salary', salary=4000)

# Charlie
charlie = Employee('Charlie', 'hourly', hours_worked=100, hourly_rate=25)

# Renee
renee = Employee('Renee', 'salary', salary=3000, contracts=4, commission_rate=200)

# Jan
jan = Employee('Jan', 'hourly', hours_worked=150, hourly_rate=25, contracts=3, commission_rate=220)

# Robbie
robbie = Employee('Robbie', 'salary', salary=2000, bonus=1500)

# Ariel
ariel = Employee('Ariel', 'hourly', hours_worked=120, hourly_rate=30, bonus=600)

print(billie.get_pay())  # Output: 4000
print(str(billie))  # Output: "Billie works on a monthly salary of 4000. Their total pay is 4000."

print(charlie.get_pay())  # Output: 2500
print(str(charlie))  # Output: "Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500."

print(renee.get_pay())  # Output: 3800
print(str(renee))  # Output: "Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800."

print(jan.get_pay())  # Output: 4410
print(str(jan))  # Output: "Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410."

print(robbie.get_pay())  # Output: 3500
print(str(robbie))  # Output: "Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500."

print(ariel.get_pay())  # Output: 4200
print(str(ariel)) 


# # Billie works on a monthly salary of 4000.  Their total pay is 4000.
# billie = Employee('Billie')

# # Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
# charlie = Employee('Charlie')

# # Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
# renee = Employee('Renee')

# # Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
# jan = Employee('Jan')

# # Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
# robbie = Employee('Robbie')

# # Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
# ariel = Employee('Ariel')
