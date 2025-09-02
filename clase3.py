"""
a = (lambda b:b**2)(2)
print(a)

z = (lambda x,y:x**y)(2,3)

print(z)
"""
"""
r = (lambda x,y:"x es mayor" if (x>y) else "x es menor que y")(4,5)
print(r)
"""
# B1E1.Valor Absoluto
#  Escriba una función lambda que reciba un número y retorne su valor absoluto.
# • Recuerde que el valor absoluto realiza lo siguiente: si el número es positivo o cero,
# devuelve el mismo número; si el número es negativo, devuelve el mismo número
# pero como valor positivo.

"""
v = float(input("Ingrese un numero, se retornara el valor absoluto : "))
r =(lambda x: x*-1 if(x<0) else x)(v)
print(r)
"""
#  B1E2 Escriba nuevamente la función de distancia euclidiana.
# • Transforme la función a una función anónima (lambda).
# • Su programa debe recibir las coordenadas por la entrada estándar y luego llamar a
# la función anónima.
# • La función anónima debe retornar la distancia euclidiana (presente el resultado
# por la salida estándar)
"""
px1 = float(input("Ingrese la cordenada x del punto 1 :"))
py1 = float(input("Ingrese la cordenada y del punto 1 :"))
px2 = float(input("Ingrese la cordenada x del punto 2 :"))
py2 = float(input("Ingrese la cordenada y del punto 2 :"))

d_euclidiana =(lambda x1,y1,x2,y2:((x2-x1)**2+(y2-y1)**2)**(0.5) )(px1,py1,px2,py2)
print(d_euclidiana)
"""

# B1E3 Escriba una función lambda que retorne el dígito verificador de un RUT.
# • La lambda debe recibir como parámetro un RUT sin dígito verificador y retornar
# este último.
# • Revise el algoritmo para dígito verificador en:
# https://es.wikipedia.org/wiki/Rol_%C3%9Anico_Tributario (sección “Procedimiento
# para obtener el dígito verificador

#Ingresa el rut sin digito verificador
"""
rut = str(input("Ingrese rut sin puntos y sin digito verificador : "))
len_rut = len(rut)
list_chr_rut = list(rut)
sn = [2,3,4,5,6,7]
sum = 0
flag = True
while (flag):
    for i in range(len(sn)):  
        if (len(list_chr_rut) > 0):
            x = int(list_chr_rut.pop()) * sn[i]
            sum = sum + x
        else:
            flag = False
# #Individualizas los numeros del rut
mod11_rest = 11 - (sum%11)
digito = mod11_rest
if mod11_rest == 11 or mod11_rest == 10:
    digito = (lambda x: 0 if mod11_rest == 10 else "K")(digito)

print(digito)
"""
# Determinar el mayor valor en una lista
# • Escriba un programa que reciba una lista y permita determinar el valor mayor.
# • Debe usar una operación tipo “reduce()” para realizar las comparaciones.
# • El programa debe imprimir por pantalla el valor mayor de la lista
"""
from functools import reduce
lista_test = [10,2,3,-5,7]

mayor_value = reduce(lambda x,y: y if (x<y) else x ,lista_test)
print(mayor_value)
 """
# Viento registrado en estaciones de monitoreo
# Cree un programa que solicite el nombre de una estación de monitoreo y los vientos registrados
# (nudos) en las últimas 5, 10, y 15 horas.
# • Almacene esta información en la memoria principal usando diccionarios y listas.
# • Su programa debe crear un nuevo diccionario con los vientos registrados en kilómetros por hora.
# • Además, el programa debe mostrar por la salida estándar el nombre de la estación y los vientos
# registrados (convertidos a kilómetros por hora).
# • Debe usar operación map().
# • Tip: los vientos en una zona calmada están entre los 3 y 10 nudos


End_program = False
stations = {}

while not End_program: 
    wind = []
    station_name = input("Ingrese el nombre de la estacion :")
    for i in range(3):
        w= float(input(f"Ingrese los vientos en nudos en las ultimas {5*(i+1)} horas) "))
        wind.append(w)
    
    wind_khr = list(map(lambda x: x*2,wind))
    stations[station_name] = {'wind_data': wind,'wind_k/hr':wind_khr}
    for key in stations:
        wind_data_khr = stations[key]['wind_k/hr']
        print(f"Estación {key}, Vientos : {wind_data_khr}")