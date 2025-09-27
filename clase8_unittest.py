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

if __name__ == '__main__':
    #La longitud varia entre 90 y -90, latitud entre 0 y 180, altura mayor a 0 y menor a 20000 metros
    #Preparacion
    posicion = Position(10,10,20)
    #Ejecucion
    def test_init_position_lat(obj,ex_lat):
        if obj.latitud == ex_lat:
            print("Latitud Correcta")
    def test_init_position_lon(obj,ex_lon):
        if obj.longitud == ex_lon:
            print("Longitud Correcta")
    def test_init_position_alt(obj,ex_alt):
        if obj.altitud == ex_alt:
            print("Altitud Correcta")


    test_init_position_lat(posicion,10)
    test_init_position_lon(posicion,10)
    test_init_position_alt(posicion, 20)