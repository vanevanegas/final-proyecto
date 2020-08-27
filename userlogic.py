from Logic import Logic
from userobj import UserObj


class UserLogic(Logic):
    def __init__(self):
        super().__init__()
        self.keys = [
            "id",
            "user",
            "password",
            "role",
            "nombre",
            "apellido",
            "email",
            "nombre_tarjeta",
            "num_tarjeta",
            "mes_venc",
            "anno_venc",
            "cvv",
            "direccion",
            "ciudad",
            "departamento",
        ]

    def getUserData(self, user):
        database = self.get_databaseXObj()
        sql = f"select * from lacocinadeapolo.usuarios where usuario='{user}';"
        data = database.executeQuery(sql)
        data = self.tupleToDictionaryList(data, self.keys)
        if len(data) > 0:
            data_dic = data[0]
            userObj = UserObj(
                data_dic["id"],
                data_dic["user"],
                data_dic["password"],
                data_dic["role"],
                data_dic["nombre"],
                data_dic["apellido"],
                data_dic["email"],
                data_dic["nombre_tarjeta"],
                data_dic["num_tarjeta"],
                data_dic["mes_venc"],
                data_dic["anno_venc"],
                data_dic["cvv"],
                data_dic["direccion"],
                data_dic["ciudad"],
                data_dic["departamento"],
            )
            return userObj
        else:
            return None
