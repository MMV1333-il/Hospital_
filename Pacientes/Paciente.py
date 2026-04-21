#Creacion de carpeta y archivo, la clase hablara sobre pacientes del hospital
class Paciente:
    def __init__(self,nombre,edad,num_expediente,alergias = [],cant_cons = 0):
        self.__nombre = nombre
        self.__edad = edad
        self.__num_expediente = num_expediente
        self.__alergias = alergias
        self.__cant_cons = cant_cons

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre):
        self.__nombre = nombre
    
    def get_edad(self):
        return self.__edad
    def set_edad(self,edad):
        self.__edad = edad

    def get_num_expediente(self):
        return self.__num_expediente
    def set_num_expediente(self,num_expediente):
        self.__num_expediente = num_expediente

    def get_alergias(self):
        return self.__alergias
    def set_alergias(self,alergias):
        self.__alergias = alergias

    def get_cant_cons(self):
        return self.__cant_cons
    def set_cant_cons(self,cant_cons):
        self.__cant_cons = cant_cons
    
    def info(self):
        print(f"numero de expediente del paciente: {self.__num_expediente}-nombre del paciente: {self.__nombre}-edad del paciente: {self.edad}")

    def registro_cons(self):
        self.__cant_cons += 1
        print("Se creo una nueva consulta")
        print(f"La cantidad de consultas es: {self.__cant_cons}")
    
# CREANDO UN OBJETO PACIENTE PARA PROBAR LA CLASE Y SUS METODOS
#SE CREO UN OBJETO
p1 = Paciente("Karla",18,2345,["Fenozoparadina","Pregabalina","Amoxicilina"])
#SE PRUEBA EL METODO INFO
p1.info()
#SE PRUEBA EL METODO REGISTRO DE CONSULTA
p1.registro_cons()
p1.registro_cons()



        