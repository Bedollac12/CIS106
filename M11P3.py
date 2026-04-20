def forecast(month, sales):
  if month == "Jan" or month == "Feb" or month == "Mar":
    percent = 0.10
  elif month == "Apr" or month == "May" or month == "Jun":
    percent = 0.15
  elif month == "Jul" or month == "Aug" or month == "Sep":
    percent = 0.20
  else:
     percent = 0.25

  next_month_sales = sales * (1 + percent)
  return next_month_sales

answer = input("Do you want to enter data? (Yes/No): ")

while answer == "Yes":
  last_name = input("Enter last name: ")
  month = input("Enter month (Jan,Feb, Mar, etc.):")
  sales = float(input("Enter sales: "))

  next_sales = forecast(month, sales)

  print("Last Name:", last_name)
  print("Next Month's Forecast:", f"{next_sales:.2f}")
  print()

  answer = input("Do you want to enter data? (Yes/No): ")