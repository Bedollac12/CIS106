names = ["Adams", "Baker", "Clark", "Davis", "Evans", "Frank", "Ghosh", "Hills", "Irwin", "Jones"]
scores = [85.5, 92.0, 78.3, 90.1, 88.7, 72.4, 95.0, 81.6, 77.9, 89.2]

def display_names(name_list, score_list):
  for i in range(len(name_list)):
    print(name_list[i], score_list[i])

def display_reverse(name_list, score_list):
  for i in range(len(name_list)-1, -1, -1):
    print(name_list[i], score_list[i])

print("Names and Scores in order:")
display_names(names, scores)
print()
print("Names and Scores in reverse:")
display_reverse(names, scores)