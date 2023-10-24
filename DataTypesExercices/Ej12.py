bread = 3.49
discount = 0.6
amountOfBreads = int(input("How many breads : "))
print(f"price of a bread {bread}€, discount {discount} and the total "+str(round((bread*discount*amountOfBreads),2)))
