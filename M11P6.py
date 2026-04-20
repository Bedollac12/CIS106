def calc_scores(score1, score2, score3):
  total = score1 + score2 + score3
  average = total / 3
  return total, average

answer = input("Do you want to enter a student? (Yes/No): ")

while answer == "Yes":
  last_name = input("Enter last name: ")
  score1 = float(input("Enter first exam score: "))
  score2 = float(input("Enter second exam score: "))
  score3 = float(input("Enter third exam score: "))

  total_pts, avg = calc_scores(score1, score2, score3)

  print("Last Name:", last_name)
  print("Total Points:", f"{total_pts:.2f}")
  print("Average:", f"{avg:.2f}")
  print()

  answer = input("Do you want to enter another student? (Yes/No): ")