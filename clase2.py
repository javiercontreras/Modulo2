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
"""
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

def mostrar_resultados():
    for j in range(estudiantes):
        print(f"El estudiante \"{db_estudiantes[j][0]}\" tiene un promedio de {db_estudiantes[j][2]}")

#Ejecucion codigo
datos_estudiantes()
mostrar_resultados()
"""
"""
programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
}

#Print an item of the dictionary
print(programming_dictionary["Bug"])
"""
# Ejemplo: Gestión de Inventario de Productos
# Considerando el enunciado anterior, realicemos lo siguiente:
# 1. Cree un diccionario llamado inventario que representará el inventario
# de la tienda. El inventario deberá contener nombre, cantidad y precio
# de tres productos.
# 2. Actualizar la cantidad de un producto solicitando los datos al usuario
# (nombre de producto a actualizar, y cantidad).
# 3. Mostrar el inventario completo recorriendo el diccionario.
"""

inventario = {"tv":{"cantidad":5,"precio":100},
              "lavadora":{"cantidad":10,"precio":200},
              "plancha":{"cantidad":0,"precio":30}}


producto = input("Ingrese el nombre del producto : ")

if producto not in inventario:
    print("Su producto no existe en el inventario")
else:
    nueva_cantidad = int(input("Ingrese el nuevo stock del producto : "))

inventario[producto]["cantidad"] = nueva_cantidad

for clave in inventario:
    print(f"El item {clave} tiene un stock de :{inventario[clave]['cantidad']}, a un precio de {inventario[clave]['precio']}.")
"""

# Desarrolla un programa que permita registrar el nombre y apellido de varias personas,
# almacenando cada registro en un diccionario y organizando todos los registros en
# una lista.
# a. Solicita al usuario los datos de cada persona. Cada persona debe ser
# almacenada en un diccionario con las claves "nombre" y "apellido".
# b. Guarda cada diccionario en una lista llamada personas. Cada vez que se
# ingresen los datos de una persona, crea un diccionario y agrégalo a la lista
# personas.
# c. El programa debe continuar solicitando datos hasta que el usuario ingrese "FIN"
# como nombre.
# d. Mostrar la lista de personas. Recorre la lista personas e imprime el nombre y
# apellido de cada persona registrada.
"""
personas = []
END = "CONTINUA"

while END != "FIN":
    registro = {"nombre":"nombre","apellido": "apellido"}
    print("Entra al ciclo")
    inombre = input("Ingrese nombre : ")
    iapellido = input("Ingrese apellido : ")
    registro['nombre'] = inombre
    registro['apellido'] = iapellido
    personas.append(registro)
    print(personas)
    END = input("Si desea terminar ingrese la palaba \"FIN\" : ").upper()

for i in personas:
    print(f"{i}")
"""
# Cursos y notas de una persona
# Incrementar la funcionalidad del programa anterior permitiendo que ahora cada
# persona cuente con cursos inscritos.
# • Es decir, necesitamos que cada persona contenga un diccionario con claves
# correspondientes a cursos y cada clave con una lista con las notas de dicho
# curso.
# • Todos los datos deben ser solicitados por la entrada estándar. Puede considerar
# ingresar un curso por persona. Cada curso tendrá 3 notas.
# • Al finalizar, el programa debe imprimir el nombre y apellido, seguido del listado de
# cursos y los promedios obtenidos en cada curso.

personas = []
END = "CONTINUA"

while END != "FIN":
    registro = {"nombre":"nombre","apellido": "apellido","cursos":{}}
    
    notas = [0,0,0]
    inombre = input("Ingrese nombre : ")
    iapellido = input("Ingrese apellido : ")
    registro['nombre'] = inombre
    registro['apellido'] = iapellido
    
    curso = input("Ingrese el nombre del curso al que deseas asistio : ")
    print ("Ingrese las 3 notas del curso al que asistio : ")
    for i in range(len(notas)):
        x = float(input(f"Ingrese la nota {i+1} : "))
        notas[i] = x
    registro["cursos"] = {curso:notas}
    personas.append(registro)
    print(personas)
    END = input("Si desea terminar ingrese la palaba \"FIN\" : ").upper()

for i in personas:
    print(f"Estudiante: {i['nombre']} {i['apellido']}")
    for clave in i['cursos']:
        notas_promedio = i['cursos'][clave]
        print(f"{clave} notas {sum(notas_promedio)/len(notas_promedio)}")
        