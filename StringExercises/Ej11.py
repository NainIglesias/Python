class Product:
	def __init__(self, name, price, unit):
		self.name = name
		self.price = price
		self.unit = unit
	def show(self):
		print(f"Name: {self.name}, Price: {self.price}, Units: {self.unit}")
productName = input("Product name: ")
productPrice = round(float(input("Product price: ")),2)
productUnits = input("Product units: ")
myProduct = Product(productName, str(productPrice).zfill(9), productUnits)
myProduct.show()

