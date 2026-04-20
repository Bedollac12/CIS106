def calc_discount(qty, price, rate):
  extended = qty * price
  discounted_amount = extended * rate
  discounted_price = extended - discounted_amount
  return discounted_amount, discounted_price

answer = input("Do you want to enter data? (Yes/No): ")

while answer == "Yes":
  qty = float(input("Enter quantity: "))
  price = float(input("Enter price: "))
  rate = float(input("Enter discount rate (example: 0.10 for 10%): "))

  disc_amt, disc_price = calc_discount(qty, price, rate)

  print("Quantity:" , qty)
  print("Price:", f"{price:.2f}")
  print("Discount Amount:", f"{disc_amt:.2f}")
  print("Discounted Price:", f"{disc_price:.2f}")
  print()

  answer = input("Do you want to enter more data? (Yes/No): ")