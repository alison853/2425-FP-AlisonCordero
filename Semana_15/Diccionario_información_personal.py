#Crea un diccionario con información ficticia sobre una persona
informacion_personal = {
    "nombre": "Sara Japón",
    "edad" : 25,
    "ciudad" : "Quito" ,
    "profesion" :"Doctora"
}

#Accerder al valor de la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Cuenca"

#Agregar una nueva clave-valor que representa el "telefono"
if "telefono" not in informacion_personal :
    informacion_personal["telefono"] = "0991321760"

# Eliminar la clave "edad" del diccionario
informacion_personal.pop("edad" , None)

#Imprimir el diccionario resultante
print("Diccionario final:" , informacion_personal)