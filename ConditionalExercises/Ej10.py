class Pizza:
    def __init__(self, ingrediente):
        self.ingrediente = ingrediente

    def show(self):
        print(f"Mozzarella, tomate, {self.ingrediente}")

eleccion = int(input("¿Pizza vegana (1) o normal (2)? "))

condimentos = {
    1: ("Pimiento", "Tofu"),
    2: ("Peperoni", "Jamón", "Salmón")
}

if eleccion == 1:
    for i, condimento in enumerate(condimentos[1], start=1):
        print(f"{i}: {condimento}")
    eleccion2 = int(input("Ingresa el número correspondiente al ingrediente: "))
    ingrediente = condimentos[1][eleccion2 - 1]
elif eleccion == 2:
    print("Elige los ingredientes:")
    for i, condimento in enumerate(condimentos[2], start=1):
        print(f"{i}: {condimento}")
    eleccion2 = int(input("Ingresa el número correspondiente al ingrediente: "))
    ingrediente = condimentos[2][eleccion2 - 1]

pizza = Pizza(ingrediente)
pizza.show()
