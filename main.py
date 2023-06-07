from library.package.module import MiClase
from library.estudiante_utils.approved import Estudiante


def module():
    # Crear una instancia de la clase
    objeto = MiClase("valor1", "valor2")

    # Acceder a los atributos y métodos de la instancia
    print(objeto.parametro1)
    print(objeto.parametro2)
    objeto.metodo1()
    objeto.metodo2()


def estudiante_utils():
    # Crear instancias de la clase Estudiante
    estudiante1 = Estudiante("Maria", 18, 8.5)
    estudiante2 = Estudiante("Gloria", 20, 6.2)

    # Imprimir información de los estudiantes
    estudiante1.imprimir_informacion()
    print("Aprobado:", estudiante1.es_aprobado(), end="\n\n")
    
    estudiante2.imprimir_informacion()
    print("Aprobado:", estudiante2.es_aprobado())


if __name__ == '__main__':
    #module()
    estudiante_utils()
