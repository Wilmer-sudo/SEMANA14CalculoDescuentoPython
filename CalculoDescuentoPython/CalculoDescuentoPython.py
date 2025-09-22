# Archivo: CalculoDescuentoPython.py

# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado a una compra.

    Parámetros:
        monto_total (float): Monto total de la compra.
        porcentaje_descuento (float): Porcentaje de descuento a aplicar (por defecto 10%).

    Retorna:
        float: Monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal
def main():
    # Primera llamada: usando el descuento por defecto (10%)
    monto1 = 1000  # Ejemplo de compra
    descuento1 = calcular_descuento(monto1)
    total_pagar1 = monto1 - descuento1

    print("=== Compra 1 ===")
    print(f"Monto total: ${monto1}")
    print(f"Descuento aplicado: ${descuento1}")
    print(f"Total a pagar: ${total_pagar1}\n")

    # Segunda llamada: indicando el porcentaje de descuento manualmente (ejemplo 15%)
    monto2 = 2000
    descuento2 = calcular_descuento(monto2, 15)
    total_pagar2 = monto2 - descuento2

    print("=== Compra 2 ===")
    print(f"Monto total: ${monto2}")
    print(f"Descuento aplicado: ${descuento2}")
    print(f"Total a pagar: ${total_pagar2}")


# Ejecución del programa
if __name__ == "__main__":
    main()
