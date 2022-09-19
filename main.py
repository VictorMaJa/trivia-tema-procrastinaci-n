#AGREGAMOS LA CLASE COLOR CON COLORES COMO PROPIEDAD
class color:
    AZUL = '\033[94m'
    ROJO = "\033[91m"
    VERDE = "\033[92m"
    AMARILLO = "\033[93m"
    NEGRITA = "\033[1m"
    CYAN = "\033[96m"
    FIN = '\033[0m'


# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print(color.AZUL,
      "¡BIENVENIDO A MI TRIVIA SOBRE EL TEMA DE LA PROCRASTINACIÓN!",
      color.FIN)

print("Pondremos a prueba tus conocimientos sobre este tema tan importante\n")

print(color.ROJO)
nombre = input("Ingresa tu Nombre Por favor: ")
print(color.FIN)

intentos = 0
print(color.AMARILLO)
while nombre == "":
    nombre = input("Tu nombre es obligatorio: ")
print(color.FIN)

if nombre not in nombre:
    print("Se ha superado el numero de intentos por favor ingrese su nombre: ")
    exit()

print("\n Hola", nombre, ":\n")
print(
    "Responde las siguientes preguntas escribiendo la letra de la alternativa corecta y presiona 'ENTER' para enviar tu respuesta:\n"
)

#Pregunta 01
print(color.NEGRITA, "1) ¿Qué es la Procrastinación?\n", color.FIN)
print("a) Proceso de formación de cosas")
print("b) Proceso de enfriamiento")
print("c) Retrasar algo que se debe hacer")
print("d) Ninguna de las anteriores")

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
respuesta_1 = input("\nTu respuesta: ")
opciones = ("a", "b", "c", "d")
intentos = 0

while respuesta_1 not in opciones and intentos <= 2:
    intentos = intentos + 1
    respuesta_1 = input(
        "Debes responder a, b, c o d. Ingresa tu respuesta por favor: ")

if respuesta_1 not in opciones:
    print("Se ha superado el numero de intentos")
    exit()

if respuesta_1 == "a":
    print(color.ROJO, "Incorrecto!!!", color.FIN)

if respuesta_1 == "b":
    print(color.ROJO, "Incorrecto!!!", color.FIN)

if respuesta_1 == "c":
    print(color.VERDE, "Correcto!!!", color.FIN)

if respuesta_1 == "d":
    print(color.ROJO, "Incorrecto!!!", color.FIN)

print("Vamos por la siguiente pregunta:\n")

#Pregunta 02
print(color.NEGRITA,
      "2) ¿Cómo te sentirías si no haces la tarea que se requiere?\n",
      color.FIN)
print("a) Alegre")
print("b) Odio")
print("c) Prometer")
print("d) Preocupación")

# Almacenamos la respuesta del usuario en la variable "respuesta_2"
respuesta_2 = input("\nTu respuesta: ")
opciones = ("a", "b", "c", "d")
intentos = 0

while respuesta_2 not in opciones and intentos <= 2:
    intentos = intentos + 1
    respuesta_2 = input(
        "Debes responder a, b, c o d. Ingresa tu respuesta por favor: ")

if respuesta_2 not in opciones:
    print("Se ha superado el numero de intentos")
    exit()

if respuesta_2 == "a":
    print(color.ROJO, "Incorrecto!!!", color.FIN)

if respuesta_2 == "b":
    print(color.ROJO, "Incorrecto!!!", color.FIN)

if respuesta_2 == "c":
    print(color.ROJO, "Incorrecto!!!", color.FIN)

if respuesta_2 == "d":
    print(color.VERDE, "Correcto!!!", color.FIN)

print("Vamos por la siguiente pregunta y Última:\n")

#Pregunta 03
print(
    color.NEGRITA,
    "3) Si pudieras hacer una cosa para cumplir con tu objetivo a tiempo, ¿cuál seria?\n",
    color.FIN)
print("a) Levantarme tarde")
print("b) Mirar el reloj")
print("c) Mantener mi compromiso")
print("d) Mentirte a ti mismo")

# Almacenamos la respuesta del usuario en la variable "respuesta_3"
respuesta_3 = input("\nTu respuesta: ")
opciones = ("a", "b", "c", "d")
intentos = 0

while respuesta_3 not in opciones and intentos <= 2:
    intentos = intentos + 1
    respuesta_3 = input(
        "Debes responder a, b, c o d. Ingresa tu respuesta por favor: ")

if respuesta_3 not in opciones:
    print("Se ha superado el numero de intentos")
    exit()

if respuesta_3 == "a":
    print(color.ROJO, "Incorrecto!!!", color.FIN)

if respuesta_3 == "b":
    print(color.ROJO, "Incorrecto!!!", color.FIN)

if respuesta_3 == "c":
    print(color.VERDE, "Correcto!!!", color.FIN)

if respuesta_3 == "d":
    print(color.ROJO, "Incorrecto!!!", color.FIN)

print(
    color.CYAN,
    "¡¡¡GRACIAS POR RESPONDER MI TRIVIA SOBRE EL TEMA DE LA PROCRASTINACIÓN!!!\n",
    color.FIN)
print(color.CYAN, "*****MUCHAS GRACIAS*****", color.FIN)
