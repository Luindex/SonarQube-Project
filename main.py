import json
import os

FILE_PATH = 'storage.json'

# Cargar productos desde archivo JSON
def load_data():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

# Guardar productos al archivo JSON
def save_data(data):
    try:
        json_string = json.dumps(data, indent=4)
        with open(FILE_PATH, 'w') as f:
            f.write(json_string)
    except Exception as e:
        print("Error al guardar el archivo:", e)
        raise

# Crear un producto
def crear_producto(producto):
    data = load_data()
    if any(p['id'] == producto['id'] for p in data):
        raise ValueError(f"El producto con ID {producto['id']} ya existe.")
    data.append(producto)
    save_data(data)
    print(f"Producto '{producto['nombre']}' registrado con éxito.")

# Leer un producto
def leer_producto(id):
    data = load_data()
    for p in data:
        if p['id'] == id:
            return p
    raise ValueError("Producto no encontrado.")

# Actualizar un producto
def actualizar_producto(id, nuevos_datos):
    data = load_data()
    for i, p in enumerate(data):
        if p['id'] == id:
            data[i].update(nuevos_datos)
            save_data(data)
            print("Producto actualizado.")
            return
    raise ValueError("Producto no encontrado.")

# Eliminar un producto
def eliminar_producto(id):
    data = load_data()
    nueva_data = [p for p in data if p['id'] != id]
    if len(nueva_data) == len(data):
        raise ValueError("Producto no encontrado.")
    save_data(nueva_data)
    print("Producto eliminado.")

# Menú interactivo
if __name__ == "__main__":
    while True:
        print("\n--- CRUD de Productos ---")
        print("1. Crear producto")
        print("2. Leer producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                producto = {
                    "id": input("ID: "),
                    "nombre": input("Nombre: "),
                    "descripcion": input("Descripción: "),
                    "precio": float(input("Precio: ")),
                    "cantidad": int(input("Cantidad: "))
                }
                crear_producto(producto)

            elif opcion == "2":
                id_producto = input("Ingrese el ID del producto a buscar: ")
                producto = leer_producto(id_producto)
                print("Producto encontrado:")
                print(json.dumps(producto, indent=4))

            elif opcion == "3":
                id_producto = input("ID del producto a actualizar: ")
                nuevos_datos = {}
                nombre = input("Nuevo nombre (Enter para omitir): ")
                if nombre:
                    nuevos_datos["nombre"] = nombre
                descripcion = input("Nueva descripción: ")
                if descripcion:
                    nuevos_datos["descripcion"] = descripcion
                precio = input("Nuevo precio: ")
                if precio:
                    nuevos_datos["precio"] = float(precio)
                cantidad = input("Nueva cantidad: ")
                if cantidad:
                    nuevos_datos["cantidad"] = int(cantidad)

                actualizar_producto(id_producto, nuevos_datos)

            elif opcion == "4":
                id_producto = input("ID del producto a eliminar: ")
                eliminar_producto(id_producto)

            elif opcion == "5":
                print("Saliendo...")
                break

            else:
                print("Opción no válida.")

        except ValueError as e:
            print("Error:", e)
        except Exception as e:
            print("Error inesperado:", e)
