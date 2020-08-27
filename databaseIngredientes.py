import mysql.connector


class DatabaseIngredientes:
    def __createCursor(self):
        con = mysql.connector.connect(
            host="localhost", user="root", passwd="12345", database="lacocinadeapolo"
        )
        cursor = con.cursor()
        return con, cursor

    def getAllIngredientes(self):
        con, cursor = self.__createCursor()
        cursor.execute("SELECT * FROM lacocinadeapolo.ingredientes;")
        data = cursor.fetchall()
        print(data, con)
        return data

    def insertIngredientes(self, ingredientes, descripcion, precio):
        con, cursor = self.__createCursor()
        sql = (
            "insert into lacocinadeapolo.ingredientes"
            + "(id, nombre, descripcion, precio) "
            + f"values(0, '{ingredientes}','{descripcion}','{precio}');"
        )
        cursor.execute(sql)
        con.commit()
        return cursor.rowcount

    def searchIngredientes(self, search):
        con, cursor = self.__createCursor()
        cursor.execute(
            f"SELECT * FROM lacocinadeapolo.ingredientes WHERE nombre LIKE '%{search}%' OR descripcion LIKE '%{search}%';"
        )
        data = cursor.fetchall()
        print(data, con)
        return data

    def getIngredienteByReceta(self, id):
        con, cursor = self.__createCursor()
        cursor.execute(
            f"SELECT recetas.nombre,ingredientes.nombre,ingredientes.id,ingredientes.precio FROM ingredientes JOIN ingredientes_por_receta ON ingredientes.id = ingredientes_por_receta.ingredientes_id JOIN recetas ON ingredientes_por_receta.recetas_id = recetas.id and recetas.id={id}"
        )
        data = cursor.fetchall()
        print(data, con)
        return data

    def insertACarrito(self, id_ingrediente, id_usuario):
        con, cursor = self.__createCursor()
        sql = f"insert into lacocinadeapolo.carrito(id,id_usuario,id_ingrediente)  values(0,{id_ingrediente},{id_usuario});"
        print(sql)
        cursor.execute(sql)
        con.commit()
        return cursor.rowcount


class DatabaseX:
    def __init__(self):
        self.__host = "localhost"
        self.__user = "root"
        self.__passwd = "12345"
        self.__database = "lacocinadeapolo"
        self.__connection = self.createConnection()
        self.__cursor = self.createCursor()

    def get_host(self):
        return self.__host

    def get_user(self):
        return self.__user

    def get_password(self):
        return self.__passwd

    def get_database(self):
        return self.__database

    def get_connection(self):
        return self.__connection

    def get_cursor(self):
        return self.__cursor

    def createConnection(self):
        con = mysql.connector.connect(
            host=self.get_host(),
            user=self.get_user(),
            passwd=self.get_password(),
            database=self.get_database(),
        )
        return con

    def createCursor(self):
        con = self.get_connection()
        cursor = None
        if con is not None and con.is_connected():
            cursor = con.cursor()
        else:
            print("app is disconnected from database")
        return cursor

    def executeQuery(self, sql):
        cursor = self.get_cursor()
        con = self.get_connection()
        result = None
        if cursor is not None and con.is_connected():
            cursor.execute(sql)
            result = cursor.fetchall()
        return result

    def executeNonQueryBool(self, sql):
        cursor = self.get_cursor()
        con = self.get_connection()
        hasAffected = False
        if cursor is not None and con.is_connected():
            cursor.execute(sql)
            con.commit()
            rows = cursor.rowcount
            if rows > 0:
                hasAffected = True
        return hasAffected

    def executeNonQueryRows(self, sql):
        cursor = self.get_cursor()
        con = self.get_connection()
        rows = 0
        if cursor is not None and con.is_connected():
            cursor.execute(sql)
            con.commit()
            rows = cursor.rowcount
        return rows
