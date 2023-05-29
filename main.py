from ArregloEmpleados import arregloEmpleados
from mPlanta import LectorPlanta
from mContratado import LectorContratados
from mExterno import LectorExternos

if __name__ == "__main__":
    # Leer empleados de los archivos
    empleados_planta = LectorPlanta.leer_archivo()
    empleados_contratados = LectorContratados.leer_archivo()
    empleados_externos = LectorExternos.leer_archivo()

    # Crear colección de empleados y agregar los empleados leídos
    arreglo_empleados = arregloEmpleados(100)

    for empleado in empleados_planta:
        arreglo_empleados.agregar_empleado(empleado)

    for empleado in empleados_contratados:
        arreglo_empleados.agregar_empleado(empleado)

    for empleado in empleados_externos:
        arreglo_empleados.agregar_empleado(empleado)

    while True:
        print("1. Registrar horas")
        print("2. Total de tarea")
        print("3. Ayuda Económica")
        print("4. Calcular sueldo")
        print("5. Salir")

        opcion=int(input("Ingresar una opcion: "))

        if opcion == 1:
            dni= int(input("Ingresar dni: "))
            horas= int(input("Ingresar cantidad de horas trabajadas en el día de la fecha: "))
            arreglo_empleados.opcion1(dni,horas)

        elif opcion==2:
            tarea= (input("Ingresar Tarea: "))
            arreglo_empleados.opcion2(tarea)

        elif opcion==3:
           print("Lista de Empleados con Ayuda Economica")
           arreglo_empleados.opcion3()
           
        
        elif opcion==4:
            print("Lista de Empleados")
            arreglo_empleados.opcion4()
            
        elif opcion==5:
            print("Saliendo del programa...")
            break
        
        else:
            print("opcion no valida")