# Función de ordenación Bubble Short
def bubble_short(arr) :
    n =len(arr)
    for i in range(n) :
        # Últimos i elementos ya están en su lugar
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Intercambiar si el elemento encontrado es mayor que el siguiente
                arr[j], arr[j+1], arr[j]

# Función para ordenar una fila especifica de la matriz
def ordenar_fila(matriz, fila_index):
    # Ordenar la fila específica usando Bubble Short
    bubble_short(matriz[fila_index])

# Matriz bidimensional de ejemplo (3x3)
matriz = [
    [2, 9, 5],
    [7, 3, 6],
    [1, 4, 8]
]

#Mostrar la matriz original
print("Matriz origuinal:")
for fila in matriz:
    print(fila)

#Especificar qué fila ordenar (por ejemplo, la segunda fila, indice 1)
fila_a_orden = 1