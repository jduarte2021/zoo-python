
class Animal:
    def __init__(self,nombre,edad,accion,felicidad=0,salud=0):
            self.nombre = nombre
            self.edad = edad
            self.accion = accion
            self.felicidad = felicidad
            self.salud = salud
            self.alimentacion = ""
            return self
    def __str__(self):
        return f"El {self.nombre}, {self.accion} Felicidad: {self.felicidad} Salud: {self.salud}"
        
    def Alimentacion(self,comida=0):
        if comida >= 50:
            self.salud += 3
            self.felicidad += 3
            print (f"Recibio {comida} kilos de comida, por lo tanto su felicidad y salud subio 3ptos")
        else:
            self.salud -= 3
            self.felicidad -= 3
            print (f"Recibio {comida} kilos de comida, por lo tanto su felicidad y salud disminuyo 3ptos")
        return self

    #def display_info(self):
        print(f"{Animal}")


# class ave (animal):
#     def acciones(self):
#         return ["volar", "comer", "respirar"]

# jack = Leon("jack",12,"Ruge",10,10)
# negro = Tigre("Negro",6,"Ruge",10,10)
# blanco = Oso("Negro",6,"Gruñe",10,10)
# #jack.alimentacion("comida")

# print(jack)
# print(negro)
# print(blanco)