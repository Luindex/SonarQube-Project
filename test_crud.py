import unittest
import os
import json
from main import crear_producto, leer_producto, actualizar_producto, eliminar_producto, FILE_PATH

class TestCRUD(unittest.TestCase):

    def setUp(self):
        # Limpiar el archivo JSON antes de cada prueba
        with open(FILE_PATH, 'w') as f:
            f.write('[]')

    def _load_data(self):
        with open(FILE_PATH, 'r') as f:
            return json.load(f)

    def test_crear_producto(self):
        producto = {
            "id": "1",
            "nombre": "Teclado",
            "descripcion": "Teclado mecánico",
            "precio": 150000.0,
            "cantidad": 10
        }
        crear_producto(producto)
        data = self._load_data()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['nombre'], "Teclado")

    def test_actualizar_producto(self):
        producto = {
            "id": "2",
            "nombre": "Mouse",
            "descripcion": "Mouse óptico",
            "precio": 50000.0,
            "cantidad": 5
        }
        crear_producto(producto)
        actualizar_producto("2", {"precio": 60000.0, "cantidad": 6})
        actualizado = leer_producto("2")
        self.assertEqual(actualizado["precio"], 60000.0)
        self.assertEqual(actualizado["cantidad"], 6)

    def test_eliminar_producto(self):
        producto = {
            "id": "3",
            "nombre": "Pantalla",
            "descripcion": "Pantalla LED",
            "precio": 300000.0,
            "cantidad": 3
        }
        crear_producto(producto)
        eliminar_producto("3")
        with self.assertRaises(ValueError):
            leer_producto("3")

    def test_flujo_completo_producto(self):
        # 1. Crear producto
        producto = {
            "id": "4",
            "nombre": "Audífonos",
            "descripcion": "Audífonos inalámbricos",
            "precio": 80000.0,
            "cantidad": 8
        }
        crear_producto(producto)
        creado = leer_producto("4")
        self.assertEqual(creado["nombre"], "Audífonos")

        # 2. Actualizar producto
        actualizar_producto("4", {"nombre": "Audífonos Bluetooth", "precio": 90000.0})
        actualizado = leer_producto("4")
        self.assertEqual(actualizado["nombre"], "Audífonos Bluetooth")
        self.assertEqual(actualizado["precio"], 90000.0)

        # 3. Eliminar producto
        eliminar_producto("4")
        with self.assertRaises(ValueError):
            leer_producto("4")

if __name__ == '__main__':
    unittest.main()
