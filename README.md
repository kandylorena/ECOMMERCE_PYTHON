# ECOMMERCE_PYTHON

# Ecommerce en Consola - Python (Módulo 3)

Este proyecto es una aplicación de comercio electrónico (Ecommerce) basada en la consola de comandos, desarrollada  en **Python 3**. El programa simula el flujo de compra de un usuario: visualizar un catálogo de productos, realizar búsquedas, gestionar un carrito de compras  y calcular totales de pago con validación de datos.
---

## 📋 Características del Proyecto (MVP)

1. **Catálogo:** Registra productos iniciales usando una lista de diccionarios con atributos únicos (`id`, `nombre`, `categoría`, `precio`).
2. Permite filtrar productos  mediante coincidencia de texto.
3. **Carrito de Compras :**
   * Controla el agregar productos mediante la validación previa de existencia de ID.
   * Restringe el ingreso de cantidades erróneas, negativas o nulas (`cantidad > 0`).
   * Acumula cantidades de manera automática si un producto idéntico vuelve a ser agregado al carrito.
   * Calcula de forma exacta los subtotales por artículo y el total global a pagar.
4. Menú  implementado con bucles de control que se repite de manera estable hasta que el usuario decida salir explícitamente (`opción 0`).

---

## 🛠️ Requisitos Técnicos e Implementación

*  El catálogo y el carrito de compras se manejan mediante listas y diccionarios independientes para aislar correctamente el origen de los datos.
* **Validación de Datos :** Uso de condicionales avanzados (`if`, `elif`, `else`)  con bloques de control de excepciones `try-except` si se introducen caracteres alfabéticos en campos numéricos (ID o Cantidades).
*  5 funciones: La función 
`buscar_productos, mostrar_menu, listar_productos, agregar_al_carrito, mostrar_carrito_y_total` 


---

## 📂 Estructura de Archivos del Entregable

```
.
├── README.md            # Código fuente unificado con el programa principal y sus funciones.
└── ecommerce_m3.py      # Documentación explicativa del sistema (este archivo).
```
```

🚀 Instrucciones de Ejecución

Tener instalado Python 3.x.

2. **Ejecución del programa:** En una terminal de comandos , navegar hasta el directorio correspondiente de la carpeta y ejecuta el comando:
   python ecommerce_m3.py
```
```
   enlace a git 
   https://github.com/kandylorena/ECOMMERCE_PYTHON.git
   ```