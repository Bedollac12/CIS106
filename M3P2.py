Stock_Symbol= input("Enter the stock symbol:")
Number_of_Shares= float(input("Enter the number of shares: "))
Cost_per_Share= float(input("Enter the cost per share: "))
Calculate_amount_invested= Number_of_Shares*Cost_per_Share
print(f"Amount invested: ${Calculate_amount_invested:.2f}")