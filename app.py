from clases.leon import Leon
from clases.oso import Oso
from clases.tigre import Tigre

jack = Leon("jack",12,"Ruge",10,10)
negro = Tigre("Negro",6,"Ruge",10,10)
blanco = Oso("Negro",6,"Gruñe",10,10)

jack.Alimentacion(60)
negro.Alimentacion(30)
blanco.Alimentacion(50)


print(jack)
print(negro)
print(blanco)