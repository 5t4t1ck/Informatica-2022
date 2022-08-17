tupla = ("Esto","es","una","tupla")
print(tupla)
print(type(tupla))

print(tupla.count("es"))
print(tupla.index("Esto"))
print(tupla[2])

lista = list(tupla)
print(lista)
print(type(lista))
lista.append("Dato agregado")
print(lista)
