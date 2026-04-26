def display_names(name_list, score_list):
  for i in range(len(name_list)):
    print(name_list[i], score_list[i])

def find_highest(name_list, score_list):
  high_score = 0
  high_index = 0
  for i in range(len(score_list)):
    if score_list[i] > high_score:
       high_score = score_list[i]
       high_index = i
  print("Highest Score:", name_list[high_index], high_score)

def find_lowest(name_list, score_list):
  low_score = 999
  low_index = 0
  for i in range(len(score_list)):
    if score_list[i] < low_score:
      low_score =  score_list[i]
      low_index = i
  print("Lowest Score:", name_list[low_index], low_score)

f = open("students.txt", "r")
names = []
scores = []

line = f.readline().rstrip('\n')

while line != "":
  names.append(line)
  score = float(f.readline())
  scores.append(score)
  line = f.readline().rstrip('\n')

f.close()

print("All Students:")
display_names(names, scores)
print()
find_highest(names, scores)
find_lowest(names, scores)