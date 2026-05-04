class Student:
  def __init__(self, first_name, last_name, district, credits):
    self.first_name = first_name
    self.last_name = last_name
    self.district = district
    self.credits = credits

  def calc_tuition(self):
    if self.district == "I":
      cost = 250.00
    else:
      cost = 500.00
    tuition = self.credits * cost
    return tuition

  def display(self):
    tuition = self.calc_tuition()
    print("Name:", self.first_name, self.last_name)
    print("District:", self.district)
    print("Credits:", self.credits)
    print("Tuition owed:", f"{tuition:.2f}")
    print()
    
student1 = Student("John", "Doe", "I", 12)
student2 = Student("Jane", "Smith", "O", 15)

student1.display()
student2.display()