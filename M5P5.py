tickets = int(input("Enter the number of concert tickets: "))
if tickets >= 25:
  price = 50
elif tickets >= 10:
  price = 60
elif tickets >= 5:
  price = 70
else:
  price = 75
total = tickets * price
print(f"{'Number of Tickets:':<25} {tickets:>10}")
print(f"{'Price Per Ticket:':<25} {price:>10.2f}")
print(f"{'Total Cost:':<25} {total:>10.2f}")