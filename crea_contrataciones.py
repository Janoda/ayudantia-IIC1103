import random
f = open("contrataciones.txt", "w")
equipos = ["Univ Católica", "U. La Calera", "Unión Española ", "Curicó Unido", "Antofagasta", "U. de Chile", "Huachipato", "U. Concepción", "Audax", "Everton", "Wanderers", "Cobresal", "Iquique", "Palestino", "Coquimbo", "O'Higgins", "La Serena", "Colo Colo" ]
newline = ''
for i in equipos:
    st = random.randint(1,3) #solo uno de cada 3 equipos contara con un goleador estrella
    if st == 1:
        f.write(newline)
        f.write(i + ';' + str(random.randint(1,4))) #agregamos al equipo i una contratacion con una destreza random entre 1 y 4
        newline = '\n'

f.close()