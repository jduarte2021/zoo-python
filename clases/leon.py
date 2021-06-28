from .animal import Animal

class Leon(Animal):
    def __init__(self,nombre,edad,accion,felicidad=10,salud=10):
        super().__init__(nombre,edad,accion,felicidad,salud)
        print (f"El Leon llamado {self.nombre} de {self.edad} años siempre {self.accion}")
        print (f"Su nivel de felicidad de 0 a 10 es de: {self.felicidad} y su salud es de: {self.salud}")
        print ("################################################################################")
        