dogs = []

def menu():
  choice = ""
  while choice != "4":
    print("Dog Rescue")
    print("----------")
    print("1. Add a Dog")
    print("2. View Dogs")
    print("3. Find Dog")
    print("4. Quit")
    print()
    choice =  input("Select a choice: ")
    print()

    if choice == "1":
      addDog()
    elif choice == "2":
      viewDogs()
    elif choice == "3":
      findDog()
    elif choice == "4":
      print("Goodbye")
    else:
      print("Invalid choice. Try again.")
      print()

def addDog():
  name = input("Dog Name: ")
  breed = input("Dog Breed: ")
  age = input("Age: ")
  weight = input("Weight: ")
  dog = {"name": name, "breed": breed, "age": age, "weight": weight}
  dogs.append(dog)
  print(name, "has been added!")
  print()

def viewDogs():
  if len(dogs) == 0:
    print("No dogs in rescue yet.")
    print()
    return
  print("Rescue Dogs")
  print("-" * 60)
  print(f"{'Dog':<15}{'Breed':<25}{'Age':<10}{'Weight':<10}")
  print("-" * 60)
  for dog in dogs:
    print(f"{dog['name']:<15}{dog['breed']:<25}{dog['age']:<10}{dog['weight']:<10}")
  print()

def findDog():
  search = input("Enter dog name to search:")
  found = False
  for dog in dogs:
    if dog["name"] == search:
      found = True
      print("Found", search)
      print("Breed:", dog["breed"])
      print("Age:", dog["age"])
      print("Weight:", dog["weight"])
      print()
  if not found:
    print("Sorry, unable to find", search)
    print()

def main():
  menu()

main()