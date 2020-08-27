import mysql.connector


class DatabasePedidos:
    def __createCursor(self):
        con = mysql.connector.connect(
            host="localhost", user="root", passwd="12345", database="lacocinadeapolo"
        )
        cursor = con.cursor()
        return con, cursor

    def getAllProd(self, idusuario):
        con, cursor = self.__createCursor()
        cursor.execute(
            f"SELECT venta.id, detalles_venta.nombre_prod, venta.cantidad FROM venta INNER JOIN detalles_venta ON venta.id=detalles_venta.id_venta and venta.usuarios_id = {idusuario};"
        )
        data = cursor.fetchall()
        print(data, con)
        return data

    def precioEnvio(self, departamento):
        con, cursor = self.__createCursor()
        sql = f"SELECT * FROM lacocinadeapolo.precio_envio where departamento = '{departamento}';"
        cursor.execute(sql)
        data = cursor.fetchone()
        print(data, con)
        return data

    def getAllPedidos(self, idpedido):
        con, cursor = self.__createCursor()
        cursor.execute(f"SELECT * FROM lacocinadeapolo.venta where id={idpedido};")
        data = cursor.fetchall()
        print(data, con)
        return data

    def enviarCarrito(self, idUsuario):
        con, cursor = self.__createCursor()
        sql = f"SELECT ingredientes.nombre,ingredientes.id,ingredientes.precio FROM ingredientes JOIN lacocinadeapolo.carrito ON ingredientes.id = carrito.id_ingrediente Join lacocinadeapolo.usuarios on carrito.id_usuario = usuarios.id and usuarios.id={idUsuario};"
        print(sql)
        cursor.execute(sql)
        data = cursor.fetchall()
        print(data, con)
        return data
