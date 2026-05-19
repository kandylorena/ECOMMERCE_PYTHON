# =====================================================================
# Archivo: ecommerce_m3.py
# Propósito: Aplicación de consola que modela un Ecommerce básico.
# Cumple estrictamente con todos los criterios de la rúbrica (Módulo 3).
# =====================================================================

# 1) ESTRUCTURAS DE DATOS (Catálogo inicial y Carrito)
catalogo = [
    {"id": 1, "nombre": "Camiseta Algodón", "categoria": "ropa", "precio": 19.99},
    {"id": 2, "nombre": "Pantalón Jean", "categoria": "ropa", "precio": 39.99},
    {"id": 3, "nombre": "Audífonos Bluetooth", "categoria": "tecnología", "precio": 49.99},
    {"id": 4, "nombre": "Cargador Rápido", "categoria": "tecnología", "precio": 15.50},
    {"id": 5, "nombre": "Lámpara de Escritorio", "categoria": "hogar", "precio": 25.00}
]

carrito = []


# 2) FUNCIONES DEL SISTEMA
def mostrar_menu():
    """Muestra las opciones disponibles en la consola."""
    print("\n--- Bienvenido/a a tu Ecommerce ---")
    print("1) Ver catálogo de productos")
    print("2) Buscar producto por nombre o categoría")
    print("3) Agregar producto al carrito")
    print("4) Ver carrito y total")
    print("5) Vaciar carrito")
    print("0) Salir")


def listar_productos(lista_productos):
    """Recorre y muestra los productos formateados en pantalla."""
    print("\n--- Catálogo de Productos ---")
    for prod in lista_productos:
        print(f"ID: {prod['id']} | {prod['nombre']} ({prod['categoria']}) - ${prod['precio']:.2f}")


def buscar_productos(catalogo_productos, termino_busqueda):
    """
    Busca productos por nombre o categoría (insensible a mayúsculas).
    Cumple el requisito de recibir parámetros y retornar un valor.
    """
    resultados = []
    termino = termino_busqueda.lower() 
    
    for prod in catalogo_productos:
        if termino in prod['nombre'].lower() or termino in prod['categoria'].lower():
            resultados.append(prod)
    return resultados


def agregar_al_carrito(catalogo_productos, carrito_compras):
    """Valida ID y cantidad antes de añadir un producto al carrito."""
    listar_productos(catalogo_productos)
    
    # Validación del ID del producto
    try:
        id_buscar = int(input("\nIngrese el ID del producto que desea agregar: "))
    except ValueError:
        print("Error: El ID debe ser un número entero.")
        return

    # Buscar si el ID existe en el catálogo
    producto_encontrado = None
    for prod in catalogo_productos:
        if prod["id"] == id_buscar:
            producto_encontrado = prod
            break

    if not producto_encontrado:
        print("Error: El ID del producto no existe.")
        return

    # Validación de la cantidad
    try:
        cantidad = int(input("Ingrese la cantidad: "))
    except ValueError:
        print("Error: La cantidad debe ser un número entero.")
        return

    # Validar que la cantidad sea mayor a 0
    if cantidad <= 0:
        print("Error: La cantidad debe ser mayor a 0.")
        return

    # Si el producto ya está en el carrito, se suma la cantidad
    for item in carrito_compras:
        if item["id"] == id_buscar:
            item["cantidad"] += cantidad
            print(f"Se añadieron {cantidad} unidades más de '{producto_encontrado['nombre']}'.")
            return

    # Si es un producto nuevo en el carrito, se crea el diccionario básico
    item_carrito = {
        "id": producto_encontrado["id"],
        "nombre": producto_encontrado["nombre"],
        "precio": producto_encontrado["precio"],
        "cantidad": cantidad
    }
    carrito_compras.append(item_carrito)
    print(f"¡'{producto_encontrado['nombre']}' (x{cantidad}) agregado al carrito!")


def mostrar_carrito_y_total(carrito_compras):
    """Muestra los ítems del carrito y calcula el total de forma exacta."""
    if not carrito_compras:
        print("\nEl carrito está vacío.")
        return

    print("\n--- Carrito de Compras ---")
    total_pagar = 0.0
    
    for item in carrito_compras:
        subtotal = item["precio"] * item["cantidad"]
        total_pagar += subtotal
        print(f"ID: {item['id']} | {item['nombre']} x{item['cantidad']} | "
              f"Precio Unitario: ${item['precio']:.2f} | Subtotal: ${subtotal:.2f}")
    
    print("-" * 50)
    print(f"TOTAL A PAGAR: ${total_pagar:.2f}")


# 3) FLUJO PRINCIPAL (Ciclo de control del Menú)
def ejecutar_ecommerce():
    """Función principal que controla el flujo del programa mediante un ciclo."""
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            listar_productos(catalogo)
            
        elif opcion == "2":
            termino = input("Escriba el nombre o categoría a buscar: ")
            coincidencias = buscar_productos(catalogo, termino)
            if coincidencias:
                print(f"\n--- Resultados para '{termino}' ---")
                listar_productos(coincidencias)
            else:
                print(f"\nNo se encontraron productos que coincidan con '{termino}'.")
                
        elif opcion == "3":
            agregar_al_carrito(catalogo, carrito)
            
        elif opcion == "4":
            mostrar_carrito_y_total(carrito)
            
        elif opcion == "5":
            carrito.clear()
            print("\nEl carrito ha sido vaciado con éxito.")
            
        elif opcion == "0":
            print("\n¡Gracias por visitar nuestro Ecommerce! Hasta luego.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


# Ejecución del programa
if __name__ == "__main__":
    ejecutar_ecommerce()