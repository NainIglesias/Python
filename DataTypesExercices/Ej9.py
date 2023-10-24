def calculaInteres(cantidad, interes, anios):
	return cantidad + (.01 * interes)*anios*cantidad
cantidad = float(input("Cantidad: "))
interes = float(input("Interes: "))
anios = int(input("Anios: "))
print(str(calculaInteres(cantidad,interes,anios)))
