import pandas as pd

datos = {
"nombres": ["Gabriela", "Juan", "Daniela", "Alberto"],
"edades": [70, 75, 78, 82]
}

personas = pd.DataFrame(datos)

print(personas)

