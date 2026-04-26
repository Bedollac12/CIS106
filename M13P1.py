names = ["Adams", "Baker","Clark", "Davis", "Evans", "Frank", "Ghosh", "Hills", "Irwin", "Jones"]

def display_names(name_list):
  for i in range(len(name_list)):
    print(name_list[i])

def display_reverse(name_list):
  for i in range(len(name_list)-1, -1, -1):
    print(name_list[i])

print("Names in order:")
display_names(names)
print()
print("Names in reverse:")
display_reverse(names)