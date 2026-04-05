Quantity = float(input("Enter the quantity: "))
if Quantity >= 1000:
  unit_price = 3.00
else:
  unit_price = 5.00
extended_price = Quantity * unit_price
tax = extended_price * 0.07
total = extended_price + tax
print(f"Quantity: {Quantity:.2f}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Extended Price: ${extended_price:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")