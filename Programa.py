import csv

def cargar_empleados(archivo):
    empleados = []

    try:
        with open("empleados.CSV", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try: 
                    empleado = {
                            "legajo": int(fila["legajo"]),
                            "nombre": fila["nombre"],
                            "area": fila["area"],
                            "dias_disponibles": int(fila["dias_disponibles"])
                    }
                    empleados.append(empleado)
                except (ValueError, KeyError):
                    print(f"Error en la fila {fila}.")
    
    except FileNotFoundError:
        print("No se encontró el archivo CSV")
    
    return empleados

def cargar_areas(archivo):
    areas = []

    try:
        with open("areas.CSV", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try: 
                    area = {
                            "area": fila["area"],
                            "cobertura_minima": int(fila["cobertura_minima"]),
                            "empleados_presentes": int(fila["empleados_presentes"])
                    }
                    areas.append(area)
                except (ValueError, KeyError):
                    print(f"Error en la fila {fila}.")
    
    except FileNotFoundError:
        print("No se encontró el archivo CSV")
    return areas

def buscar_empleado(empleados, legajo):
    for empleado in empleados:
        if empleado ["legajo"] == legajo:
            return empleado
    
        return None


empleados = cargar_empleados("empleados.csv")
areas = cargar_areas("areas.csv")

while True:
    try:
        legajo = int(input("Ingrese su legajo: "))

        empleado = buscar_empleado(empleados, legajo)

        if empleado is not None:
            break

        print("Legajo inválido. Intente nuevamente.")

    except ValueError:
        print("Debe ingresar únicamente números.")

    print("Legajo inválido. Intente nuevamente.")

print(f"Bienvenido {empleado['nombre']}.")
print(f"Del área de: {empleado['area']}.")
print(f"Cuentas con: {empleado['dias_disponibles']} días disponibles.")

intentos = 0

while intentos < 3:

    dias = int(input("Ingrese la cantidad de días solicitados: "))

    if dias <= empleado["dias_disponibles"]:
        print("Cantidad de días válida.")
        break

    intentos += 1

    print(
        f"No posee días suficientes. "
        f"Intento {intentos} de 3."
    )

else:

    print("\nLa solicitud no pudo ser procesada debido a múltiples intentos inválidos.")
    print("\nSu consulta ha sido derivada al sector de Recursos Humanos.")

    




