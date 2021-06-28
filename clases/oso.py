from .animal import Animal
class Oso(Animal):
    def __init__(self,nombre,edad,accion,felicidad=0,salud=0):
        super().__init__(nombre,edad,accion,felicidad,salud)
        print (f"El Oso llamado {self.nombre} de {self.edad} años siempre {self.accion}")
        print (f"Su nivel de felicidad de 0 a 10 es de: {self.felicidad} y su salud es de: {self.salud}")
        print ("################################################################################")