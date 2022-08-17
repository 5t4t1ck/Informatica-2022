diccionario = {
    "nombre":"Diego",
    "apellido":"Saavedra",
    "edad":34
}
print(diccionario)
print(type(diccionario))

print(diccionario["edad"])
print(diccionario.get("apellido"))

diccionario["nombre"] = "Juanito"
print(diccionario["nombre"])
print(len(diccionario))

diccionario["sexo"]= "Masculino"
print(diccionario)

diccionario.pop("sexo")
print(diccionario)