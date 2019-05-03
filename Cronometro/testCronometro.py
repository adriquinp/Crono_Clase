from Cronometro import *

x=input("Ingrese una hora:")


c= Cronometro()
c.setTiempo(x)
for i in range(1000):
    c.retroceder()
    print c.getTiempo()


    
