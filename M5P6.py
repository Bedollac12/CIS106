last_name = input("Enter employee last name: ")
salary = float(input("Enter employee salary: "))
job_level = int(input("Enter employee job level: "))
if job_level >= 10:
  bonus_rate = 0.25
elif job_level >= 5:
  bonus_rate = 0.20
else:
  bonus_rate = 0.10
bonus = salary * bonus_rate
print("Employee Last Name:", last_name)
print("Bonus:", f"{bonus:.2f}")