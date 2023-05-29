import csv
from claseExterno import EmpleadoExterno

class LectorExternos:
    @staticmethod
    def leer_archivo():
        empleados_externos = []

        with open("externos.csv", "r") as file:
            reader = csv.reader(file)
            cabecera=True
            for row in reader:
                if cabecera:
                    cabecera=False
                else:
                    dni, nombre, direccion, telefono, tarea, fecha_inicio, fecha_fin, monto_viatico, costo_obra, monto_seguro_vida = row
                    empleado = EmpleadoExterno(int(dni), nombre, direccion, telefono, tarea, fecha_inicio, fecha_fin, float(monto_viatico), float(costo_obra), float(monto_seguro_vida))
                    empleados_externos.append(empleado)

        return empleados_externos
