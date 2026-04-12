count = 0

answer = input("Do you want to enter a student? (Yes/No): ")

while answer == "Yes":
  last_name = input("Enter last name: ")
  score1 = float(input("Enter first exam score: "))
  score = float(input("Enter second exam score: "))

  average = (score1 + score) / 2

  print("Last Name: ", last_name)
  print("Average Score: ", average)

  count = count + 1

  answer = input("Do you want to enter another student? (Yes/No): ")

print("Number of students: ", count)