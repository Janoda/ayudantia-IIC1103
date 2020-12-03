import random
f = open("resultados.txt", "w")
equipos = ["Univ Católica", "U. La Calera", "Unión Española ", "Curicó Unido", "Antofagasta", "U. de Chile", "Huachipato", "U. Concepción", "Audax", "Everton", "Wanderers", "Cobresal", "Iquique", "Palestino", "Coquimbo", "O'Higgins", "La Serena", "Colo Colo" ]
newline = ''
for i in equipos:
    for j in equipos:
        if i == j:
            continue 
        else:
            f.write(newline)
            gol1 = str(random.randint(0,5))
            gol2 = str(random.randint(0,5))
            f.write(i+';'+j+';'+gol1 + '-'+gol2)
            newline = '\n'
f.close()