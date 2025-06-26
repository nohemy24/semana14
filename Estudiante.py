import os 
import getpass
import pwinput
#Se importa el modulo os para usar la funcion: os.path.exists(rute)
ARHIVO = "Estudiantes.txt"

#Crear usuarios .py - para agregar usuarios
#Def agregarusuario(usuario, clave):
    #with open("usuarios.txt", "a") as archivo:
        #archivo.write(f"{usuario},{clave}\n")
#Ejemplo de uso:
#agregarusuario("Admin", "Admin1234")
#agregarusuario("juan", "clave1234")

#Función para cargar archivo: usuarios.txt
def cargarusuarios():
    usuarios = {}
    if os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "r") as archivo:
            for linea in archivo:
                usuario,clave = linea.strip().split(",")
                usuarios[usuario] = clave
    return usuarios

def cargarestudiantes():
    estudiantes = []
    #La funcion os.path.exists(rute) verifica si el archivo existe en una ruta determinada
    if os.path.exists(ARHIVO):
        with open(ARHIVO, "r") as file:
            for line in file:
                codigo, nombre, edad, carrera = line.strip().split(",")
                #Linea.strip() elimina los espacios en blanco al inicio y al final de la cadena
                #Split(",") divide la cadena en una lista usando la coma como separador
                estudiantes.append({
                    "codigo": codigo,
                    "nombre": nombre,
                    "edad": int(edad),
                    "carrera": carrera
                })
    return estudiantes

def guardarestudiantes(estudiantes):
    with open(ARHIVO, "w") as archivo:
        for est in estudiantes:
            linea=f"{est['codigo']},{est['nombre']},{est['edad']},{est['carrera']}\n"
            archivo.write(linea)

def crearestudiante(estudiantes):
    codigo=input("Código de estudiante: ")
    #Verificar si el código ya existe
    #LA funcion any() devuelve True si al menos un elemento del iterable es verdadero
    if any (est["codigo"] == codigo for est in estudiantes):
        print("El código ya existe.")
        return estudiantes
    
    nombre=input("Nombre del estudiante: ")
    apellido=input("Apellido del estudiante: ")
    carrera=input("Carrera del estudiante: ")

    estudiantes.append({
        "codigo": codigo,
        "nombre": f"{nombre} {apellido}",
        "edad": 0,  # Edad se puede actualizar más tarde
        "carrera": carrera
    })
    guardarestudiantes(estudiantes)
    print("Estudiante agregado correctamente.\n")

def mostrarestudiantes(estudiantes):
    if not estudiantes:
        print("\nLista de estudiantes:")
        return

    print("\nLista de estudiantes:")
    for est in estudiantes:
        print(f"Código: {est['codigo']}, Nombre: {est['nombre']}, Edad: {est['edad']}, Carrera: {est['carrera']}")
        print()

def actualizarestudiante(estudiantes):
    codigo=input("Ingresa el código del estudiante a actualizar: ")
    for est in estudiantes:
        if est["codigo"] == codigo:
            est["nombre"] = input("Nuevo nombre del estudiante: ")
            est["apellido"] = input("Nuevo apellido del estudiante: ")
            est["carrera"] = input("Nueva carrera del estudiante: ")
            guardarestudiantes(estudiantes)
            print("Estudiante actualizado correctamente.\n")
            return
    print("Estudiante no encontrado.\n")

def eliminarestudiante(estudiantes):
    codigo=input("Ingresa el código del estudiante a eliminar: ")
    for est in estudiantes:
        if est["codigo"] == codigo:
            estudiantes.remove(est)
            guardarestudiantes(estudiantes)
            print("Estudiante eliminado correctamente.\n")
            return
    print("Estudiante no encontrado.\n")

# Función principal para interactuar con el usuario
def menu():
    estudiantes=cargarestudiantes()
    while True:
        print("===== MENÚ CRUD ESTUDIANTES =====")
        print("1. Crear estudiante")
        print("2. Leer estudiantes")
        print("3. Actualizar estudiante")
        print("4. Eliminar estudiante")
        print("5. Salir")
        opcion=input("Selecciona una opción: ")
        if opcion == "1":
            crearestudiante(estudiantes)
        elif opcion == "2":
            mostrarestudiantes(estudiantes)
        elif opcion == "3":
            actualizarestudiante(estudiantes)
        elif opcion == "4":
            eliminarestudiante(estudiantes)
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

#Definir variables con la contraseña
ARCHIVO = "Estudiantes.txt"
CLAVE = "Admin1234"

#Función para verificar la contraseña
def inicio():
    print("===== INICIO DE SESIÓN =====")
    usuarios = cargarusuarios()
    usuario = input("Ingresa tu usuario: ")
    #ntento=input("Ingresa la contraseña: ")
    #intento = getpass.getpass("Ingresa la contraseña: ")  # Usar getpass para ocultar la entrada
    claveingresada=pwinput.pwinput(prompt='contraseña: ', mask='*')  # Usar pwinput para ocultar la entrada
    if usuario in usuarios and usuarios[usuario] == claveingresada == claveingresada:
        print("Acceso concedido.\n")
        return True
    else:
        print("Usuario o contraseña incorrectos.\n")
        return False

#Llamada a la función para ejecutar inicio antes de mostrar el menú
if inicio():
    menu()