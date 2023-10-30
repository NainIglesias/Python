price = round(float(input("Price with 2 decimals: ")),2)
integer_part = str(price).split('.')[0]
decimal_part = str(price).split('.')[1]
print("Price integer: "+integer_part)
print("Price decimal: "+decimal_part)
