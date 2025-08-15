#BLoque A
# 1. Cree una lista inicial de productos fija.
# 2. Solicita al usuario que agregue tres nuevos productos.
# 3. Elimina un producto específico.
# 4. Ordena la lista en orden alfabético.
# 5. Muestra el primer y último producto en orden alfabético
"""
lista = ["tv","microondas","refrigerador"]

print("Ingrese tres nuevos productos")

for i in range(3):
    nuevo_elemento = str(input(f"Ingrese el nuevo elemento {i+1} :"))
    lista.append(nuevo_elemento)

print(f"Elimine un elemento de la lista{lista}")
eliminar = str(input("Ingrese el elemento que desea eliminar :"))
lista.remove(eliminar)
print(f"La lista queda ahora de esta manera : {lista}")

lista.sort()
print(f"Primer elemento de la lista : {lista[0]},y ultimo elemento de la lista es :{lista[-1]}")
"""
#Ejercicio1
# a. Crear una lista con los siguientes números:
# 10, 20, 5, 60, 20, 10 (en este orden).
# b. Determine el rango del conjunto de números.
# c. Determine el promedio haciendo uso del ciclo for.
# d. Determine el promedio haciendo uso de las funciones genéricas que
# aplican sobre la lista.

"""
lista_numeros = [10,20,5,60,20,10]
rango_menor = min(lista_numeros)
rango_mayor = max(lista_numeros)

print(f"El rango de la lista es de {rango_menor} a {rango_mayor}.")
promedio = 0
total = 0
for num in lista_numeros:
    promedio += num
    total += 1
promedio = promedio / total
print(f"El promedio de la lista de numeros es : {promedio}")

promedio_2 = sum(lista_numeros) / len(lista_numeros)
print(f"Promedio con funciones genericas = {promedio_2}")
"""

#Ejercicio2
# Desarrolle un programa que permita almacenar y calcular el promedio de notas
# de cinco estudiantes en una escuela. Cada estudiante tiene tres calificaciones
# en un rango de 1 a 7. El sistema debe solicitar los datos de los estudiantes y sus
# notas al usuario y luego mostrar el promedio de calificaciones de cada
# estudiante.
# a. Crear un programa que solicite el nombre de cada uno de los cinco
# estudiantes. Para cada estudiante, solicite tres notas.
# b. Almacenar los datos de cada estudiante (nombre y lista de notas) en una
# lista de listas.
# c. Calcular el promedio de notas para cada estudiante. Mostrar el nombre de
# cada estudiante junto con su promedio.

#Declaro variables a utilizar

nombre = str("Nan")
promedio = float(0.0)
estudiantes = int(2)
db_estudiantes = []
for i in range(estudiantes):
    notas = [float(0.0),float(0.0),float(0.0)]
    db_estudiantes.append([nombre, notas,promedio])

#Defino funciones
def inicio():
    print("Esta aplicacion entrega  el promedio de 5 estudiantes, debe ingresar el nombre y 3 notas")

def datos_estudiantes():
    
    for i in range(estudiantes):
        promedio = 0
        print("-----------------------")
        db_estudiantes[i][0] = str(input(f"Ingresar el nombre del estudiante {i+1} : "))
        for nota in range(3):
            input_nota = float(input(f"Ingrese la nota {nota+1} : "))
            db_estudiantes[i][1][nota] = input_nota
            promedio += input_nota
        db_estudiantes[i][2] = promedio/len(notas)

datos_estudiantes()
print(db_estudiantes)
for j in range(estudiantes):
    print(f"El estudiante \"{db_estudiantes[j][0]} tiene un promedio de {db_estudiantes[j][2]}")