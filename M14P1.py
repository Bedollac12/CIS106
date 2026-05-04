class Employee:
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@company.com'

  def calc_bonus(self, rate):
    bonus = self.pay * rate
    return bonus

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print("Employee:", emp_1.first, emp_1.last)
print("Email:", emp_1.email)
print("Salary:", emp_1.pay)
bonus_rate = float(input("Enter bonus rate (example 0.10 for 10%): "))
bonus = emp_1.calc_bonus(bonus_rate)
print("Bonus:", f"{bonus:.2f}")
print()

print("Employee:", emp_2.first, emp_2.last)
print("Email:", emp_2.email)
print("Salary:", emp_2.pay)
bonus_rate = float(input("Enter bonus rate (example 0.10 for 10%): "))
bonus = emp_2.calc_bonus(bonus_rate)
print("Bonus:", f"{bonus:.2f}")