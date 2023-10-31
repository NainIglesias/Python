class Product:
	def __init__(self, name, price, unit):
		self.name = name
		self.price = price
		self.unit = unit
	def show(self):
		print(f"Name: {self.name}, Price: {self.price}, Units: {self.unit}")
def rellenarCeros(string):
	for x in range(1, len(str(string)) + 1):
		print(str(x))
productName = input("Product name: ")
productPrice = round(float(input("Product price: ")),2)
productUnits = input("Product units: ")
myProduct = Product(productName, str(productPrice), productUnits)
myProduct.show()
rellenarCeros(productPrice)

