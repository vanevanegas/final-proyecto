import mysql.connector
from flask import Flask, render_template, request, redirect, session


class Database:
    def __createCursor(self):
        con = mysql.connector.connect(
            host="localhost", user="root", passwd="12345", database="lacocinadeapolo"
        )
        cursor = con.cursor()
        return con, cursor

    def getAllCourse(self):
        con, cursor = self.__createCursor()
        cursor.execute("SELECT * FROM lacocinadeapolo.usuarios;")
        data = cursor.fetchall()
        print(data, con)
        return data

    def insertCourse(self, name, contrasenna, correo):
        con, cursor = self.__createCursor()
        sql = (
            "insert into lacocinadeapolo.usuarios"
            + "(id, usuario, contrasenna,tipo,email) "
            + f"values(0, '{name}','{contrasenna}','Miembro','{correo}');"
        )
        cursor.execute(sql)
        con.commit()
        return cursor.rowcount

    def checkUser(self, name):
        con, cursor = self.__createCursor()
        cursor.execute(
            f"SELECT * FROM lacocinadeapolo.usuarios where usuario='{name}';"
        )

        data = cursor.fetchall()
        print(data)
        if len(data) == 0:
            return True
        else:
            return False

    def updateUser(
        self,
        name,
        apellido,
        direccion,
        ciudad,
        departamento,
        nombre_tarjeta,
        num_tarjeta,
        mes_venc,
        anno_venc,
        cvv,
    ):
        con, cursor = self.__createCursor()
        iduser = session["id"]
        sql = f"UPDATE lacocinadeapolo.usuarios SET nombre = '{name}', direccion='{direccion}',apellido = '{apellido}', ciudad='{ciudad}', departamento='{departamento}', nombre_tarjeta = '{nombre_tarjeta}', numero_tarjeta='{num_tarjeta}', mes_vencimiento='{mes_venc}', anno_vencimiento = '{anno_venc}', cvv='{cvv}' WHERE id = '{iduser}';"
        print(sql)
        cursor.execute(sql)
        con.commit()
        return cursor.rowcount

    def loginUser(self, username, contrasenna):
        con, cursor = self.__createCursor()
        sql = f"SELECT * FROM lacocinadeapolo.usuarios WHERE usuario = '{username}' AND contrasenna = '{contrasenna}'"
        cursor.execute(sql)
        account = cursor.fetchone()
        if account:
            # Create session data, we can access this data in other routes
            sessionLogin = True

            # Redirect to home page
            return sessionLogin
        else:
            # Account doesnt exist or username/password incorrect
            msg = "Incorrect username/password!"
        con.commit()


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
