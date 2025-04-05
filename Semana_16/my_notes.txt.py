# Abrir archivo para escritura
Archivo = open('my_notes.txt' , 'w')
#Escribir 3 líneas
Archivo.write('Mañana tengo cita con el doctor por mi embarazo.\n' )
Archivo.write('Luego tengo que ir al escuela por mi sobrino.\n')
Archivo.write('Mañana sera un día pesado pero almenos vere a mi sob rino.\n')
# Cerrar el archivo despues de escribir
Archivo.close()

#Abrir archivo para lectura
Archivo = open('my_notes.txt' , 'r')
#Indicar que se lee línea a línea y eliminar saltos de línea extras
print(Archivo.readline().strip())
print(Archivo.readline().strip())
print(Archivo.readline().strip())
#Cerrar el archivo
Archivo.close()