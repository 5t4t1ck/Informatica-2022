"""class Base1:
    pass

class Base2:
    pass

class MultipleDerivada(Base1, Base2):
    pass"""

class Perro1():

    def __init__(self, raza):
        self.raza = raza

    def ladrido(self):
        print(f"Yo tengo un ladrido fuerte y mi raza es {self.raza}")

class Perro2():
    
    def __init__(self, edad):
        self.edad = edad

    def comer(self):
        print(f"Yo como mucha croqueta, y soy {self.edad}")

class Perro3(Perro1, Perro2):
    pass

Rocky = Perro3(raza="salchicha",edad= 2)
print(Rocky.comer())
print(Rocky.ladrido())