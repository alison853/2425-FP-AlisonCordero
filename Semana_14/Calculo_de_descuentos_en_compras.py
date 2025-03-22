def calcular_descuento(monto_total, porcentaje_descuento=15):
    """
    Calcula el monto del descuento en función del porcentaje dado.
    :param monto_total: float - Monto total de la compra
    :param porcentaje_descuento: float - Porcentaje de descuento (por defecto es 15%)
    :return: float - Monto del descuento
    """
    descuento= (monto_total * porcentaje_descuento) / 100
    return descuento

#Llamadas a la función
monto1 = 125.0
monto2 = 330.0
porcentaje_descuento2 = 30

descuento1= calcular_descuento(monto1)
descuento2 = calcular_descuento(monto2, porcentaje_descuento2)

# Cálculo del monto final a pagar
monto_final1 = monto1 - descuento1
monto_final2 = monto2 -descuento2

# Mostrar resultados
print(f"Compra 1 : Monto total : ${monto1:.2f}, Descuento:${descuento1: .2f}, monto final: ${monto_final1: .2f}")
print(f"Compra 2 : Monto total : ${monto2:.2f}, Descuento:${descuento2: .2f}, monto final: ${monto_final2: .2f}")