
#Ejercicio1.1
# Elaborar el código para el cálculo de la raíz cuadrada de un número
# • Restricción: no se puede usar sqrt de la biblioteca de Python.
# • Debe solicitar el número por la entrada estándar e imprimir el resultado

"""
Ejercicio1
x = float(input("Ingrese el numero al que desea calcular su raiz cuadrada : "))
x_root = x ** (1/2)

print(f"La raiz del numero ingresado {x} es : {x_root}")
"""
#Ejercicio1.2
# • Elaborar un código para el cálculo de la distancia euclidiana entre dos puntos.
# • Recuerde que la distancia euclidiana se calcula en base a las coordenadas x e y
# de ambos puntos.
# • Debe solicitar las coordenadas de los puntos por la entrada estándar e imprimir la
# distancia

"""
x1 = float(input("Ingrese la cordenada x del punto 1 :"))
y1 = float(input("Ingrese la cordenada y del punto 1 :"))
x2 = float(input("Ingrese la cordenada x del punto 2 :"))
y2 = float(input("Ingrese la cordenada y del punto 2 :"))

d_euclidiana = ((x2-x1)**2 + (y2-y1)**2)** (1/2)

print(f"La distancia euclidiana es :  {d_euclidiana}")
"""

# Ejercicio1.3
#  Escriba un programa que solicite al usuario una palabra.
# • Invierta la palabra y guárdela en una nueva variable.
# • Imprima por pantalla la palabra original y luego la palabra invertida.

"""
palabra = str(input("Ingrese una palabra : "))
palabra_inversa = palabra[::-1]
print(f"La palabra invertida es : {palabra_inversa}")
"""


# Ejercicio 2.1
# Tomar los tres casos del trabajo grupal anterior y re escribirlos como funciones 

def root(x):  
    x_root = x ** (1/2)
    return x_root


a = float(input("Ingrese un numero para calcular su raiz : "))
b = root(a)
print(b)