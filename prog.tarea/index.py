
def calcular_total(precio1, precio2, precio3):
    total = precio1 + precio2 + precio3

    if total > 10000:
        total = total * 0.9  # 10% descuento

    if total > 20000:
        total = total * 0.8  # 20% descuento

    return total


def mostrar_ticket(cliente, total, cantidad):
    print("Cliente:", cliente)
    print("Cantidad de productos:", cantidad)
    print("Total a pagar: $", total)
    print("--------------------------")


def contar_productos(p1, p2, p3):
    productos = [p1, p2, p3]
    contador = 0

    for producto in productos:
        if producto > 0:
            contador += 1

    return contador


print("=== Tienda de ropa ===")

cliente = input("Nombre del cliente: ")

precio1 = float(input("Precio producto 1: "))
precio2 = float(input("Precio producto 2: "))
precio3 = float(input("Precio producto 3: "))


total = calcular_total(precio1, precio2, precio3)
cantidad = contar_productos(precio1, precio2, precio3)

mostrar_ticket(cliente, total, cantidad)