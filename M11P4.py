def calc_price(msrp, make, model, ev_code):
  if ev_code == "Y":
    percent = 0.30
  elif make == "Honda" and model == "Accord":
    percent = 0.10
  elif make == "Toyota" and model == "Rav4":
    percent = 0.15
  else:
    percent = 0.05

  discount = msrp * percent
  new_msrp = msrp - discount
  tax = new_msrp * 0.07
  total = new_msrp  + tax
  return total

total_msrp = 0.0
total_sales = 0.0

answer = input("Do you want to enter a vehicle? (Yes/No): ")

while answer == "Yes":
   make = input("Enter the make of the vehicle: ")
   model = input("Enter the model of the vehicle: ")
   ev_code = input("Is the vehicle an EV? (Y/N): ")
   msrp = float(input("Enter the MSRP of the vehicle: "))

   out_the_door = calc_price(msrp, make, model, ev_code)

   total_msrp = total_msrp + msrp
   total_sales = total_sales + out_the_door

   print("Make: ", make)
   print("Model: ", model)
   print("MSRP: ", f"{msrp:.2f}")
   print("Out the Door Price: ", f"{out_the_door:.2f}")
   print()

   answer = input("Do you want to enter another vehicle? (Yes/No): ")

print("Total of All MSRPs:", f"{total_msrp:.2f}")
print("Total of All Sales:", f"{total_sales:.2f}")