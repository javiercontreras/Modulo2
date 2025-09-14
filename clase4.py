# #Principios de Diseño Oientado a Objetos

# class Persona:
#     def __init__(self, nombre):
#         self.nombre = nombre

#     def get_nombre(self ):
#         return self.nombre
    

# x = Persona("Juan")
# print(x.get_nombre())\

# Ejercicio1
# Cree las clases Waypoint y Trackpoint.
# • La clase Waypoint contiene un nombre; la clase Trackpoint contiene una fecha de
# registro.
# • Ambas clases son posiciones geográficas de tipo Position.
# • La clase Position requiere en su inicialización una latitud, una longitud y una altitud
# Santiago: -33.445° de latitud Sur y -70.682° de longitud Oeste.
# La Serena: -29.906° de latitud Sur y -71.234° de longitud Oeste.
#Distancia geodesica 400km aprox
import geopy.distance

class Position:
    def __init__(self, latitud, longitud, altitud):
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

    def km(self):
        return geopy.distance.geodesic(self.coordenada1, self.coordenada2)
    
    def cordenadas(self):
        return f"{self.coordenada1} y {self.coordenada2}"

santiago = Position(-33.445,-70.682,1000)
laserena = Position(-29.906,-71.234,0)

distancia = Distance(santiago.latitud,santiago.longitud,laserena.latitud,laserena.longitud)

print(distancia.km())