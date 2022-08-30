class Perro():
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"El perro se llama {self.nombre} y tiene {self.edad} año de edad"

    def ladrar(self):
        print(f"Yo soy {self.nombre} y puedo ladrar")

perro1 = Perro("Leo", 1)
perro2 = Perro("Rocky", 2)

print(perro1)
print(perro2)

perro1.ladrar()
perro2.ladrar()
