from Motocicleta import *
class Tienda(Motocicleta):
    def __init__(self,color,matricula,combustible_litros,numero_ruedas,marca,modelo,fecha_fabricacion,velocidad_punta,peso,precio,motor=False):
        super().__init__(color,matricula,combustible_litros,numero_ruedas,marca,modelo,fecha_fabricacion,velocidad_punta,peso,motor)
        self.__precio=precio

    def getPrecio(self):
        return self.__precio
       
    def setPrecio(self,precio):
        self.__precio=precio

    def getDescripcion(self):
        return "El precio de la motocicleta " + self.getMarca() + " modelo " + self.getModelo() + " es de " + str(self.getPrecio())
       
moto3 = Tienda("VERDE","d54140","90 LITROS","2","LEGACY","2023","2022","250 km/h","35k",280000)
print(moto3.getDescripcion())