from datetime import datetime
correctAnswer = False
while not correctAnswer:
	try:
		inputDate = input("Date format dd/mm/yyyy: ")
		date = datetime.strptime(inputDate, "%d/%m/%Y")
		#print("Parsed date:",date)
		days = date.day
		months = date.month
		years = date.year
		correctAnswer = True
	except ValueError:
		print("Invalid date format\n")
print(f"Days: {days}\nMonths: {months}\nYears: {years}")
