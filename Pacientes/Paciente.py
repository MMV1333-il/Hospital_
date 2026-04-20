#Creacion de carpeta y archivo, la clase hablara sobre pacientes del hospital
class Paciente:
    def __init__(self,nombre,edad,num_expediente,alergias,hist_cons):
        self.__nombre = nombre
        self.__edad = edad
        self.__num_expediente = num_expediente
        self.__alergias = alergias
        self.__hist_cos = hist_cons

    
