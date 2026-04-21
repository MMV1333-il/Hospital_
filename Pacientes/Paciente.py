#Creacion de carpeta y archivo, la clase hablara sobre pacientes del hospital
#CONSTRUCTOR
class Paciente:
    def __init__(self,nombre,edad,num_expediente,alergias = [],cant_cons = 0):
        self.__nombre = nombre
        self.__edad = edad
        self.__num_expediente = num_expediente
        self.__alergias = alergias
        self.__cant_cons = cant_cons
    #GETTERS Y SETTERS
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
    #METODO INFO, MUESTRA DATOS BREVES DEL PACIENTE
    def info(self):
        print(f"numero de expediente del paciente: {self.__num_expediente}-nombre del paciente: {self.__nombre}-edad del paciente: {self.__edad}")
    #METODO REGISTRO DE CONSULTA, LE REGISTRA AL PACIENTE UNA CONSULTA Y LE INDICA CUANTAS CONSUTAS HA TENIDO
    def registro_cons(self):
        self.__cant_cons += 1
        print("Se creo una nueva consulta")
        print(f"La cantidad de consultas es: {self.__cant_cons}")
    #METODO COMPROBAR ALERGIAS, SI AL PACIENTE SE LE RECETA MEDICINA  SE PUEDE COMPROBAR SI ESTA EN SU LISTA DE ALERGIAS
    def comp_alergias(self,medicina):
        if medicina in self.__alergias:
            print("¡ADVERTENCIA! no recetar al paciente el medicamento: {medicina}, ya que el paciente es alergico")
        else:
            print("Es seguro recetar este medicamento")

# CREANDO UN OBJETO PACIENTE PARA PROBAR LA CLASE Y SUS METODOS
#SE CREO UN OBJETO
p1 = Paciente("Karla",18,2345,["Fenozoparadina","Pregabalina","Amoxicilina"])
p2 = Paciente("Andres",25,4863,["Hioscina","Fenozoparadina","Ciprofloxaxina"])
#SE PRUEBA EL METODO INFO
p1.info()
p2.info()
#SE PRUEBA EL METODO REGISTRO DE CONSULTA
p1.registro_cons()
p1.registro_cons()
p2.registro_cons()
#SE PRUEBA EL METODO COMPROBACION DE ALERGIA
p1.comp_alergias("Metroproclamida")
p2.comp_alergias("Hioscina")


        