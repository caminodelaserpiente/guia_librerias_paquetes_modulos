class Estudiante:
    def __init__(self, nombre, edad, promedio):
        self.nombre = nombre
        self.edad = edad
        self.promedio = promedio

    def imprimir_informacion(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Promedio:", self.promedio)

    def es_aprobado(self):
        if self.promedio >= 7.0:
            return True
        else:
            return False

