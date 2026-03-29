Purchase_price_per_share=float(input("Enter purchase price per share: "))
Stock_price=float(input("Enter stock price: "))
Quantity_of_stock=float(input("Enter quanity of stock: "))
Calculate_value_change=(Stock_price-Purchase_price_per_share)*Quantity_of_stock
print(f"Value change: {Calculate_value_change:.2f}"