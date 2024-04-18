# inventario que permita realizar el control detallado de productos en un negocio.

class producto:
    def __init__(self, codigo, nombre, valor_compra, valor_venta, stock_minimo, stock_maximo, proveedor):
        self.codigo = codigo
        self.nombre = nombre
        self.valor_compra = valor_compra
        self.valor_venta = valor_venta
        self.stock_actual = 0
        self.stock_minimo = stock_minimo
        self.stock_maximo = stock_maximo
        self.proveedor = proveedor

    def actualizar_stock(self, cantidad):
        self.stock_actual += cantidad

    def calcular_ganancia_potencial(self):
        return (self.valor_venta - self.valor_compra) * self.stock_actual

    def __str__(self):
        return f'Código: {self.codigo}\nNombre: {self.nombre}\nValor de compra: {self.valor_compra}\nValor de venta: {self.valor_venta}\nStock actual: {self.stock_actual}\nStock mínimo: {self.stock_minimo}\nStock máximo: {self.stock_maximo}\nProveedor: {self.proveedor}\n'


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    def actualizar_stock(self, codigo, cantidad):
        for producto in self.productos:
            if producto.codigo == codigo:
                producto.actualizar_stock(cantidad)
                break

    def generar_informe_productos_criticos(self):
        productos_criticos = [producto for producto in self.productos if producto.stock_actual < producto.stock_minimo]
        if productos_criticos:
            print("Productos críticos:")
            for producto in productos_criticos:
                print(producto)
        else:
            print("No hay productos críticos.")

    def calcular_ganancia_potencial_total(self):
        ganancia_total = 0
        for producto in self.productos:
            ganancia_total += producto.calcular_ganancia_potencial()
        return ganancia_total



def main():
    inventario = Inventario()
    producto1 =producto("001", "Producto 1", 10, 20, 5, 50, "Proveedor A")
    producto2 =producto("002", "Producto 2", 15, 25, 5, 50, "Proveedor B")
    inventario.agregar_producto(producto1)
    inventario.agregar_producto(producto2)

    print("Productos registrados:")
    inventario.mostrar_productos()

    inventario.actualizar_stock("001", 10)

    inventario.generar_informe_productos_criticos()

    ganancia_total = inventario.calcular_ganancia_potencial_total()
    print(f"Ganancia potencial total: ${ganancia_total}")


if __name__ == "__main__":
    main()