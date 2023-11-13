puntuacion = float(input("Puntuation: "))
condiciones = (puntuacion == 0.0, puntuacion == 0.4, puntuacion >= 0.6)
for x in condiciones:
    if x:
        print("Dinero:" + str(puntuacion*2400))
