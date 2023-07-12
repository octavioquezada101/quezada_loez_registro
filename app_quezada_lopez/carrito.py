class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
    
    def agregar_carrito(self, Productos):
        id = str(Productos.id)
        if id not in self.carrito.keys():
                self.carrito[id]={
                     "producto_id": Productos.id,
                     "nombre": Productos.nombre_produ,
                     "valor": Productos.valor,
                     "acumulado": Productos.valor,
                     "cantidad":1,
                }
        else:
             self.carrito[id]["cantidad"] += 1
             self.carrito[id]["acumulado"] += Productos.valor
        self.guardar_carrito()

    def guardar_carrito(self):
         self.session["carrito"] = self.carrito
         self.session.modified = True

    def eliminar(self, Productos):
        id = str(Productos.id)
        if id in self.carrito:
             del self.carrito[id]
             self.guardar_carrito()

    def restar(self, Productos):
        id = str(Productos.id)
        if id in self.carrito.keys():
             self.carrito[id]["cantidad"] -=1
             self.carrito[id]["acumulado"] -= Productos.valor
             if self.carrito[id]["cantidad"] <= 0: self.eliminar(Productos)
             self.guardar_carrito()
    
    def limpiar(self):
            self.session["carrito"] = {}
            self.session.modified = True