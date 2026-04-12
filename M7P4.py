f = open("items.txt", "r")

total_ep = 0.0
count = 0

item = f.readline().rstrip('\n')

while item != "":
  quantity = float(f.readline())
  price = float(f.readline())

  ep = quantity * price
  total_ep = total_ep + ep
  count = count + 1

  print("Item:", item)
  print("Quantity:", quantity)
  print("Price:", price)
  print("Extended Price:", ep)
  print()

  item = f.readline().rstrip('\n')

f.close()

average = total_ep / count
print("Total Extended Prices:", total_ep)
print("Number of Orders:", count)
print("Average Order:", average)