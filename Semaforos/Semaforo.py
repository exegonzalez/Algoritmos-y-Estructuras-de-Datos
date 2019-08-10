from TDA_Colas_Nodos_Sem import TCola, Encolar, Desencolar, ColaVacia
from PyQt5.QtTest import QTest
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi

class Semaforo():#se crea la clase semaforo
    def __init__(self, id, color, tiempo):
        self.id = id
        self.color= color
        self.tiempo= tiempo

class Principal(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("ventanasemaforo.ui", self)
        self.show()
        self.cola = TCola() #crea la cola
        pixmap = QPixmap('Fondo.png')
        self.fondo.setPixmap(pixmap)
        pixmap = QPixmap('configuracion.png')
        self.configuracion.setPixmap(pixmap)
        self.crear_sem()#llama la funcion crear semaforos
        self.tiempos = [10000] * 4
        self.semaforos = [self.sem1, self.sem2, self.sem3, self.sem4]
        self.aplicar.clicked.connect(self.configurar)
        self.empezar.clicked.connect(self.empezarciclo)

    def crear_sem (self):
        Sem1=Semaforo("1","rojo",10000)#crea los 4 objetos semaforos (son registros con los campos: id, color, tiempo)
        Sem2=Semaforo("2","rojo",10000)
        Sem3=Semaforo("3","rojo",10000)
        Sem4=Semaforo("4","rojo",10000)    
        pixmap = QPixmap('SemaforoRO.png')#crea los 4 semaforos de la interfaz y les asigna la foto del rojo
        self.sem1.setPixmap(pixmap)
        self.sem2.setPixmap(pixmap)
        self.sem3.setPixmap(pixmap)
        self.sem4.setPixmap(pixmap)
        Encolar(self.cola,Sem1)#encola los 4 semaforos a la cola
        Encolar(self.cola,Sem2)
        Encolar(self.cola,Sem3)
        Encolar(self.cola,Sem4)
        
    def empezarciclo(self,cola):
        pixmap = QPixmap('SemaforoRO.png')#crea los 4 semaforos de la interfaz y les asigna la foto del rojo
        self.sem1.setPixmap(pixmap)
        self.sem2.setPixmap(pixmap)
        self.sem3.setPixmap(pixmap)
        self.sem4.setPixmap(pixmap)
        while (not(ColaVacia(self.cola))):#hace que el ciclo de cambiar color se ejecute infinitamente
            self.CambiarColor(self.cola)#llama a la funcion cambiar color
    
    def configurar(self):
        t1 = int(self.leer1.text())
        t2 = int(self.leer2.text())
        t3 = int(self.leer3.text())
        t4 = int(self.leer4.text())
        tiempo = [t1,t2,t3,t4]
        self.tiempos = tiempo
        
    def CambiarColor(self,cola):#funcion cambiar color
        for i in range (0,4):#un ciclo for de 0 a 4 para que desencole los 4 semaforos
            x = Desencolar(cola)
            semaforo = self.semaforos[i]#es una variable que se reutiliza para manejar el semaforo de la interfaz
            x.color = "Verde"#se cambia de color el campo color del semaforo
            pixmap = QPixmap('SemaforoVE.png')#se carga la foto del semaforo en verde
            semaforo.setPixmap(pixmap)#se muestra la foto del semaforo en verde
            if(x.tiempo!=self.tiempos[i]):
                x.tiempo = self.tiempos[i]
            QTest.qWait(x.tiempo)#se le dice que muestre el semaforo verde el tiempo que esta indicado en el campo tiempo del semaforo
            x.color = "Amarillo"#se cambia de color el campo color del semaforo
            pixmap = QPixmap('SemaforoAM.png')#se carga la foto del semaforo en amarillo
            semaforo.setPixmap(pixmap)#se muestra la foto del semaforo en amarillo
            QTest.qWait(2000)#se le dice que muestre el semaforo amarillo por 5 seg
            x.color = "Rojo"#se cambia de color el campo color del semaforo
            pixmap = QPixmap('SemaforoRO.png')#se carga la foto del semaforo en rojo
            semaforo.setPixmap(pixmap)#se muestra la foto del semaforo en rojo
            Encolar(cola,x)#se vuelve a encolar el semaforo desencolado y continua ejecutandose el for con los otros semaforos que faltan

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Principal()
    sys.exit(app.exec_()) 