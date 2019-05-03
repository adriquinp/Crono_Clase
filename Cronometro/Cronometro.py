from Hora import *
from Minuto import *
from Segundo import *
from Decima import *
class Cronometro ():
    def __init__(self):
        self.h=Hora()
        self.m=Minuto()
        self.s=Segundo()
        self.d=Decima()
    def avanzar(self):
        self.d.avanzar()
        if self.d.getValor()==0:
            self.s.avanzar()
            if self.s.getValor()==0:
                self.m.avanzar()
                if self.m.getValor()==0:
                    self.h.avanzar()
    def retroceder(self):
        self.d.retroceder()
        if self.d.getValor()== self.d.getTope():
            self.s.retroceder()
            if self.s.getValor()==self.s.getTope():
                self.m.retroceder()
                if self.m.getValor()==self.m.getTope():
                    self.h.retroceder()

    def setTiempo(self, a):
        lista = a.split(":")
        self.h.setValor(int(lista[0]))
        self.m.setValor(int(lista[1]))
        self.s.setValor(int(lista[2]))
        self.d.setValor(int(lista[3]))
            

    def getTiempo(self):
        return str(self.h.getValor()).zfill(2)+":"+str(self.m.getValor()).zfill(2)+":"+str(self.s.getValor()).zfill(2)+":"+str(self.d.getValor()).zfill(2)
                
