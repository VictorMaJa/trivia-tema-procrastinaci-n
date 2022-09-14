# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print ("Bienvenido a mi trivia sobre La Procrastinación\n")
print ("Pondremos a prueba tus conocimientos sobre este tema tan importante\n")

nombre = input("Ingresa tu Nombre Por favor: ")
print("\n Hola", nombre, ":\n")
print ("Responde las siguientes preguntas escribiendo la letra de la alternativa corecta y presionando 'ENTER' para enviar tu respuesta:\n")

#Pregunta 01
print ("1) ¿Qué es la Procrastinación?\n")
print ("a) Proceso de formación de cosas")
print ("b) Proceso de enfriamiento")
print ("c) Retrasar algo que se debe hacer")
print ("d) Ninguna de las anteriores")
# Almacenamos la respuesta del usuario en la variable "respuesta_1"
respuesta_1 = input("\nTu respuesta: ")

while respuesta_1 not in ("a", "b", "c", "d"):
  respuesta_1 = input("Debes responder a, b, c o d. Ingresa tu respuesta por favor: ")

if respuesta_1 == "a":
    print ("Incorrecto!!!")
  
if respuesta_1 == "b":
    print ("Incorrecto!!!")
  
if respuesta_1 == "c":
    print("Muy Bien!!!")

if respuesta_1 == "d":
    print ("Incorrecto!!!")
  
print ("Vamos por la siguiente pregunta:\n")

#Pregunta 02
print ("2) ¿Cómo te sentirías si no haces la tarea que se requiere?\n")
print ("a) Alegre")
print ("b) Odio")
print ("c) Prometer")
print ("d) Preocupación")
# Almacenamos la respuesta del usuario en la variable "respuesta_2"
respuesta_2= input("\nTu respuesta: ")

while respuesta_2 not in ("a", "b", "c", "d"):
  respuesta_2 = input("Debes responder a, b, c o d. Ingresa tu respuesta por favor: ")

if respuesta_2 == "a":
    print ("Incorrecto!!!")
  
if respuesta_2 == "b":
    print ("Incorrecto!!!")
  
if respuesta_2 == "c":
    print("Incorrecto!!!")

if respuesta_2 == "d":
    print ("Muy Bien!!!")

print ("Vamos por la siguiente pregunta y Última:\n")

#Pregunta 03
print ("3) Si pudieras hacer una cosa para cumplir con tu objetivo a tiempo, ¿cuál seria?\n")
print ("a) Levantarme tarde")
print ("b) Mirar el reloj")
print ("c) Mantener mi compromiso")
print ("d) Mentirte a ti mismo")
# Almacenamos la respuesta del usuario en la variable "respuesta_3"
respuesta_3= input("\nTu respuesta: ")

while respuesta_3 not in ("a", "b", "c", "d"):
  respuesta_3 = input("Debes responder a, b, c o d. Ingresa tu respuesta por favor: ")

if respuesta_3 == "a":
    print ("Incorrecto!!!")
  
if respuesta_3 == "b":
    print ("Incorrecto!!!")
  
if respuesta_3 == "c":
    print("Muy Bien!!!")

if respuesta_3 == "d":
    print ("Incorrecto!!!")

print ("GRACIAS POR RESPONDER MI TRIVIA SOBRE EL TEMA DE LA PROCRASTINACIÓN:\n")
print ("MUCHAS GRACIAS")