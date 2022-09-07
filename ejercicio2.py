#En este segundo ejercicio, tendréis que crear un archivo py 
# y dentro crearéis una clase Vehículo, 
# haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.

import pickle

class Vehiculo:
    def __init__(self,marca,modelo,precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        
coche = Vehiculo('ford', 'mustang', 34000)
#necesitamos anadir la "b" al ser binario para serializarlo
f = open('datoscoche.bin','wb')
pickle.dump(coche,f)
f.close()

#Ejemplo de lectura de archivo binario
f = open('datoscoche.bin','rb')
coche = pickle.load(f)

print(coche.modelo)

