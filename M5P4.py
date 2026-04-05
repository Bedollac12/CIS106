principal= float(input("enter the principal amount: "))
year= int(input("enter the years to maturity: "))
if principal>100000 and year==5:
  interest=0.06
elif principal >= 50000 and principal <=100000 and year ==10:
  interest=0.05
elif principal >= 50000 and principal <=100000 and year ==5:
  interest=0.04
else:
  interest=0.02
first_year_interest=principal*interest
print(f"principal amount: {principal}")
print(f"interest rate: {interest}")
print(f"interest for the first year:{first_year_interest}")