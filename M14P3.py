class Student:
  tuition_rates = {
    "I": 250.00,
    "O": 500.00,
    "X": 800.00,
    "G": 250.00
  }

  def __init__(self, first_name, last_name, district, credits):
    self.first_name = first_name
    self.last_name = last_name
    self.district = district
    self.credits = credits

  def calc_tuition(self):
    rate = Student.tuition_rates[self.district]
    tuition = self.credits * rate
    return tuition

  def display(self):
    tuition = self.calc_tuition()
    print("Name:", self.first_name, self.last_name)
    print("District:", self.district)
    print("Credits:", self.credits)
    print("Tuition Owed:", f"{tuition:.2f}")
    print()

student1 = Student("Chris", "Bedolla", "I", 12)
student2 = Student("John", "Smith", "O", 15)
student3 = Student("Yuki", "Tanaka", "X", 10)
student4 = Student("Sarah", "Johnson", "G", 14)

student1.display()
student2.display()
student3.display()
student4.display()