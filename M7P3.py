f = open("employees.txt" , "r")

total_bonus= 0.0

last_name= f.readline().rstrip('\n')

while last_name !="":
  salary= float(f.readline())
 
  if salary >= 100000:
    bonus_rate= 0.20
  elif salary == 50000:
    bonus_rate = 0.15
  else:
    bonus_rate = 0.10
 
  bonus= salary * bonus_rate
  total_bonus= total_bonus + bonus
 
  print("Last_name:", last_name)
  print("Salary:", salary)
  print("bonus:" , bonus)
  print()

  last_name= f.readline().rstrip('\n')

f.close()
print("Total Bonuses Paid:", total_bonus)