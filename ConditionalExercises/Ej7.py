rents = (range(0,10000),range(10001,20000),range(20001,35000),range(35001,60000),range(60001,100000))
percents = (5,15,20,30,45)
rent = int(input("Rent:"))
for index, rent_range in enumerate(rents):
    if rent in rent_range:
        percentage = percents[index]
        print(f"The rent falls in range {index+1} with a {percentage}% increase.")
        break
else:
    print("Rent range not found.")