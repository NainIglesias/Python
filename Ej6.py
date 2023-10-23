number = int(input("Write a number to calculate the sum of all numbers to n: "))
count = 0
amount = range(1,number)
for i in amount:
	count+=i
count = count + number
print("The amunt of numbers before "+str(number)+" are " +str(count))

