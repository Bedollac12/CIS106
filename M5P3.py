part = input("Enter the part number: ")
quantity = float(input("Enter the quantity: "))
if part == "10" or part == "55":
    unit_cost = 1.00
elif part == "99":
    unit_cost = 2.00
elif part == "80" or part == "70":
    unit_cost = 3.00
else:
    unit_cost = 5.00
total_cost = quantity * unit_cost
print(f"part: {part}")
print(f"unit_cost: {unit_cost:.2f}")
print(f"total_cost: {total_cost:.2f}")
