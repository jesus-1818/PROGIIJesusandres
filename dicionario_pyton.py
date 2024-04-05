perro = {}

perro ["nombre"] = "Beru"
perro["color"] = "Negro"
perro["Raza"] = "FILA BRASILEÑO"
perro["Patas"] = "4"
perro["edad"] = "3"

estudiante = {
    
    "nombre":"Jesus",
    "apellido":"Garcia",
    "sexo":"por favor",
    "edad":"17",
    "estado civil":"bien rico",
    "habilidades":["rapidez, inteligencia, Op"],
    "pais":"Colombia",
    "Ciudad":"Cartegena",
    "Direccion":"enrique segoviano",
}

print(estudiante)
print(len(perro))
print(estudiante["habilidades"])
estudiante["habilidades"].append("vision")
print(estudiante["habilidades"])
keys = estudiante.keys()
print(keys)
values = estudiante.values()
print(values)
print(estudiante.items())
estudiante.pop("estado civil")
print(estudiante)
print(estudiante.clear())