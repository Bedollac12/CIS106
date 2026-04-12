f = open("students.txt", "r")

total_tuition = 0.0
count = 0

last_name = f.readline().rstrip('\n')

while last_name != "":
  district = f.readline().rstrip('\n')
  credits = float(f.readline())

  if district == "I":
    cost_per_credit = 250.00
  else:
     cost_per_credit = 500.00

  tuition = credits * cost_per_credit
  total_tuition = total_tuition + tuition
  count = count + 1

  print("Last Name: ", last_name)
  print("Credits:", credits)
  print("Tuition Owed:", tuition)
  print()

  last_name = f.readline().rstrip('\n')

f.close()

print("Total Tuition Owed: ", total_tuition)
print("Number of Students:", count)