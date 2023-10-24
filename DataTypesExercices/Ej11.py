def savings(amount, years):
	totalSaved = 0;
	sec = range(1,years)
	for i in sec:
		amount+=amount*0.04
	return round(totalSaved+amount,2)
amount = float(input("Amount to save: "))
years = int(input("Years saving: "))
print("Total saved: " + str(savings(amount,years)))
