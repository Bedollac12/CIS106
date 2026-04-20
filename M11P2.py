def calc_average(hits, at_bats):
  average = hits / at_bats
  return average

count = 0

answer = input("Do you want to enter a player? (Yes/No): ")

while answer == "Yes":
  last_name =  input("Enter the player's last name: ")
  hits = float(input("Enter the number of hits: "))
  at_bats = float(input("Enter the number of at bats: "))

  batting_avg = calc_average(hits, at_bats)

  print("Last Name:", last_name)
  print("Batting Average:", f"{batting_avg:.3f}")
  print()

  count = count + 1

  answer = input("Do you want to enter a player? (Yes/No): ")
print("Number of Players:", count)  