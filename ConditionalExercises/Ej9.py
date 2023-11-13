edad = int(input("Edad: "))
precios_por_rango = {
        (0, 4): 0,
        (5, 18): 5,
        (19, float('inf')): 10
}
for rango, costo in precios_por_rango.items():
        if rango[0] <= edad <= rango[1]:
            print(f"Costo para la edad {edad}: {costo}€")
  
