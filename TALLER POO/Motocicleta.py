class Motocicleta:
    def __init__(self, color, matricula, combustible_litros, numero_ruedas, marca, modelo, fecha_creacion, velocidad_punta, peso, motor = False, estado = "Nuevo") -> None:
        self.__color = color
        self.__matricula = matricula
        self.__combustible_litros = combustible_litros
        self.__numero_ruedas = numero_ruedas
        self.__marca = marca
        self.__modelo = modelo
        self.__fecha_creacion = fecha_creacion
        self.__velocidad_punta = velocidad_punta
        self.__peso = peso
        self.__motor = motor
        self.__estado = estado

    def getColor(self):
        return self.__color
    
    def setColor(self, color):
        self.__color = color
    
    def getMatricula(self):
        return self.__matricula
    
    def setMatricula(self, matricula):
        self.__matricula = matricula
    
    def getCombustible_Litros(self):
        return self.__combustible_litros
    
    def setCombustible_Litros(self, combustible_litros):
        self.__combustible_litros = combustible_litros
    
    def getNumero_Ruedas(self):
        return self.__numero_ruedas
    
    def setNumero_Ruedas(self, numero_ruedas):
        self.__numero_ruedas = numero_ruedas
    
    def getMarca(self):
        return self.__marca
    
    def setMarca(self, marca):
        self.__marca = marca
    
    def getModelo(self):
        return self.__modelo
    
    def setModelo(self, modelo):
        self.__modelo = modelo

    def getFecha_Creacion(self):
        return self.__fecha_creacion
    
    def setFecha_Creacion(self, fecha_creacion):
        self.__fecha_creacion = fecha_creacion

    def getVelocidad_Punta(self):
        return self.__velocidad_punta 
    
    def setVelocidad_Punta(self, velocidad_punta):
        self.__velocidad_punta = velocidad_punta

    def getPeso(self):
        return self.__peso
    
    def setPeso(self, peso):
        self.__peso = peso

    def getMotor(self):
        return self.__motor
    
    def setMotor(self, motor):
        self.__motor = motor

    def setEstado(self, motor):
        self.__motor = motor

    def getEstado(self):
        return self.__estado
    
    def setEstado(self, estado):
        self.__estado = estado
    
    def arrancar(self):
        if self.__motor:
            print("El motor ya estaba en marcha")
        else:
            self.__motor = True
            print("El motor ha arrancado.")
    def detener(self):
        if (not self.__motor):
            print("El motor ya estaba detenido")
        else:
            self.__motor == False
            print("El motor se ha detenido")

moto = Motocicleta("RojO", "H2321", 10, 4, "Ducati", "2021", "2023-04-29", "70KM", "29Kg")
moto2 = Motocicleta("Negro", "G2186", "", 4,"Harley Davidson", "2021", "2006-01-27", "120Km", "34Kg")
print(moto.getEstado())
print(moto.getMotor())
moto.detener()
moto.arrancar()
moto.arrancar()
moto.detener()
print(moto2.getEstado())
print(moto2.getMotor())
moto2.detener()
moto2.arrancar()
moto2.arrancar()
moto2.detener()