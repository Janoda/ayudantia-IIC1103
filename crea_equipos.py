import random
f = open("equipos.txt", "w")
equipos = ["Univ Católica", "U. La Calera", "Unión Española ", "Curicó Unido", "Antofagasta", "U. de Chile", "Huachipato", "U. Concepción", "Audax", "Everton", "Wanderers", "Cobresal", "Iquique", "Palestino", "Coquimbo", "O'Higgins", "La Serena", "Colo Colo" ]

# Asignamos una posicion aleatoria a cada equipo.
for i in range(len(equipos)):
    pos = random.randint(1,3)
    if pos == 1:
        equipos[i] += ";4-3-3"
    elif pos == 2:
        equipos[i] += ';5-2-2-1'
    else:
        equipos[i] += ";4-1-2-1-2"

# Truquito para que no quedemos con una linea vacia al final del archivo, 
# agregamos newline al comienzo y para el primero no agregamos nada.
newline = ""
for i in equipos:
    f.write(newline)
    f.write(i)
    newline = "\n"
f.close()