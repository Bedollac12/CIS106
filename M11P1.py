def comptotal(qty, price):
  total = qty * price
  if total  > 10000.00:
    total = total * 0.90
  return total

total_ext_price = 0.0

answer = input("Do you want to enter an item? (Yes/No): ")

while answer == "Yes":
  qty = float(input("Enter quantity: "))
  price = float(input("Enter price: "))

  ext_price = comptotal(qty, price)
  total_ext_price = total_ext_price + ext_price

  print("Quantity:", qty)
  print("Price:", price)
  print("Extended Price:", f"{ext_price:.2f}")
  print()

  answer = input("Do you want to enter another item? (Yes/No): ")

print("Total Extended Price:", f"{total_ext_price:.2f}")