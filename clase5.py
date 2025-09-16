"""
import geopy.distance

class Position:
    def __init__(self, latitud, longitud, altitud):

        if type(latitud) == str or type(longitud) == str or type(altitud) == str:
            raise ValueError("El valor es un palabra, se necesita un valor numerico")
        if latitud >= 90 or latitud <= -90:
            raise ValueError("Valor fuera de rango, latitud debe ser mayor o igual a -90 y menor o igual a 90 grados")
        if latitud >= 180 or latitud <= -180:
            raise ValueError("Valor fuera de rango, longitud debe ser mayor o igual a -180 y menor o igual a 180 grados")
        if altitud < 0 :
            raise ValueError("Valor fuera de rango, altitud debe ser mayor a 0 metros")
    
        self.latitud = latitud
        self.longitud = longitud
        self.altitud = altitud
    
    def text(self):
        return f"{self.latitud},{self.longitud}, {self.altitud}"
    
    def dict_Data(self):
        data = {'latitud':self.latitud, 'longitud':self.longitud,'altitud':self.altitud}
        return data

class Waypoint(Position):
    def __init__(self, latitud, longitud, altitud, nombre):
        super().__init__(latitud, longitud,altitud)
        self.nombre = nombre

class Trackpoint(Position):
    def __init__(self, latitud, longitud, altura, fecha):
        super().__init__(latitud, longitud, altura)
        self.fecha = fecha

class Distance():
    def __init__(self,x1,y1,x2,y2):
        self.coordenada1 = (x1,y1)
        self.coordenada2 = (x2,y2)

    # def km(self):
    #     return geopy.distance.geodesic(self.coordenada1, self.coordenada2)
    
    def cordenadas(self):
        return f"{self.coordenada1} y {self.coordenada2}"

santiago = Position(-33.445,-70.682,1000)
laserena = Position(-29.906,-71.234,0)
x1 = float(input("Ingrese la latitud de Santiago : "))
distancia = Distance(santiago.latitud,santiago.longitud,laserena.latitud,laserena.longitud)
print(distancia.km())
"""

"""

try:
    print("Hola Mundo"["a"])
except IndexError as error:
    print("¡¡El índice está fuera del string!!")
except TypeError as error:
    print("Una excepción ha ocurrido:", type(error).__name__, " -> ", error)
    # Una excepción ha ocurrido: TypeError -> string indices must be integers
finally:
    print("IndexError y TypeError chequeadas.")

"""
#Ejercicio1 Incorpore el siguiente código en su IDE y estúdielo
FIN = False

listado_llamados = []
while not FIN:
    registro_llamado = {"frecuencia": None, "motivo": None, "fecha": None}
    frecuencia = input("Ingrese frecuencia: ")
    if frecuencia == "FIN":
        FIN = True
    else:
        motivo = input("Ingrese motivo: ")
    fecha = input("Ingrese fecha: ")
    registro_llamado["frecuencia"] = frecuencia
    registro_llamado["motivo"] = motivo
    registro_llamado["fecha"] = fecha
    listado_llamados.append(registro_llamado)

print(listado_llamados)