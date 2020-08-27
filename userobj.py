class UserObj:
    def __init__(
        self,
        id,
        user,
        password,
        role,
        nombre,
        apellido,
        email,
        nombre_tarjeta,
        num_tarjeta,
        mes_venc,
        anno_venc,
        cvv,
        direccion,
        ciudad,
        departamento,
    ):
        self.id = id
        self.user = user
        self.password = password
        self.role = role
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.nombre_tarjeta = nombre_tarjeta
        self.num_tarjeta = num_tarjeta
        self.mes_venc = mes_venc
        self.anno_venc = anno_venc
        self.cvv = cvv
        self.direccion = direccion
        self.ciudad = ciudad
        self.departamento = departamento
