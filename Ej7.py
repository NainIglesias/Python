import math
def ims(weight, heigth):
	return weight/(math.pow(heigth,2))
weigth = float(input("weight: "))
heigth = float(input("heigth: "))
print("Your ims is: "+str(ims(weigth,heigth)))
