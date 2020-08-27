from flask import Flask, render_template, request, redirect, session, flash, url_for
from database import Database
from databaseRecetas import DatabaseRecetas
from databasePedidos import DatabasePedidos
from databaseIngredientes import DatabaseIngredientes
from MethodUtil import MethodUtil
from werkzeug.security import generate_password_hash, check_password_hash
from userlogic import UserLogic
from userobj import UserObj
import os
from upload import app as app
import urllib.request
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecretkey"

ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg", "gif"])


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/recetas", methods=["GET", "POST"])
def recetas():
    databaseReceta = DatabaseRecetas()
    if request.method == "GET":
        dataRecetas = databaseReceta.getAllRecetas()

        return render_template("recetas.html", dataRecetas=dataRecetas)
    else:

        return redirect("/recetas")


@app.route("/vista_recetas/<int:id>", methods=["GET", "POST"])
def vista_recetas(id):
    databaseReceta = DatabaseRecetas()
    databaseIngredientes = DatabaseIngredientes()
    if request.method == "GET":
        dataRecetas = databaseReceta.getRecetaById(id)
        dataIngredientes = databaseIngredientes.getIngredienteByReceta(id)
        print(dataRecetas)
        return render_template(
            "vista_recetas.html",
            dataRecetas=dataRecetas,
            dataIngredientes=dataIngredientes,
            id=id,
        )
    else:
        idusuario = session["id"]
        ingredientes = request.form.getlist("ingredientes")
        print(idusuario)
        print(ingredientes)
        for i in ingredientes:

            rows = databaseIngredientes.insertACarrito(idusuario, i)

        return redirect("/carreta")


@app.route("/ingredientes", methods=["GET", "POST"])
def ingredientes():
    databaseIngredientes = DatabaseIngredientes()
    if request.method == "GET":
        dataIngredientes = databaseIngredientes.getAllIngredientes()

        return render_template("ingredientes.html", dataIngredientes=dataIngredientes)
    else:
        search = request.form["search"]
        dataIngredientes2 = databaseIngredientes.searchIngredientes(search)
        return render_template("search.html", dataIngredientes2=dataIngredientes2)


@app.route("/search", methods=["GET", "POST"])
def searchIngredientes():
    return render_template("search.html")


@app.route("/ingresarIngrediente", methods=["GET", "POST"])
def ingresarIngredientes():
    databaseIngredientes = DatabaseIngredientes()
    if request.method == "GET":
        return render_template("ingresarIngrediente.html")
    else:
        print(request.form)
        ingredientes = request.form["ingrediente"]
        descripcion = request.form["descripcion"]
        precio = request.form["precio"]
        rows = databaseIngredientes.insertIngredientes(
            ingredientes, descripcion, precio
        )

        return redirect("/ingredientes")


@app.route("/ingresarReceta", methods=["GET", "POST"])
def ingresarReceta():
    databaseReceta = DatabaseRecetas()
    databaseIngredientes = DatabaseIngredientes()
    dataIngredientes = databaseIngredientes.getAllIngredientes()
    if request.method == "GET":
        return render_template("ingresarReceta.html", dataIngredientes=dataIngredientes)
    else:

        receta = request.form["receta"]
        descripcion = request.form["descripcion"]
        tipo = request.form["tipo"]
        video = request.form["video"]
        imagen = request.form["imagen"]
        ingredientes = request.form.getlist("ingredientes")
        print(ingredientes)
        rows = databaseReceta.insertRecetas(receta, descripcion, tipo, video, imagen)
        return redirect("/recetas")


@app.route("/ingresarImagen")
def upload_form():
    return render_template("ingresarImagen.html")


@app.route("/ingresarImagen", methods=["POST"])
def upload_image():
    print(f"request.files -> {request.files}")
    if "file" not in request.files:
        flash("No file part")
        print(request.url)
        return redirect(request.url)
    file = request.files["file"]
    print(f"file.filename -> {file.filename}")
    if file.filename == "":
        flash("No image selected for uploading")
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join("static/images/", filename))
        flash("Image successfully uploaded and displayed")
        return render_template("ingresarImagen.html", filename=filename)
    else:
        flash("Allowed image types are -> png, jpg, jpeg, gif")
        return redirect(request.url)


# app.config["UPLOAD_FOLDER"


@app.route("/agregarIngredientesARecetas/<int:id>", methods=["GET", "POST"])
def agregarIngredientesARecetas(id):
    databaseIngredientes = DatabaseIngredientes()
    databaseReceta = DatabaseRecetas()
    if request.method == "GET":

        dataIngredientes = databaseIngredientes.getAllIngredientes()

        return render_template(
            "agregarIngredientesARecetas.html", dataIngredientes=dataIngredientes, id=id
        )
    else:
        ingredientes = request.form.getlist("ingredientes")
        delete = databaseReceta.deleteIngresienteParaEditar(id)
        for i in ingredientes:

            rows = databaseReceta.insertIngredientesPorReceta(i, id)

        return redirect("/recetas")


@app.route("/carreta")
def carreta():
    databasePedidos = DatabasePedidos()

    idusuario = session["id"]
    dataCarrito = databasePedidos.enviarCarrito(idusuario)
    total = 0
    for i in dataCarrito:

        total = total + i[2]
    print(dataCarrito)
    return render_template("shopping.html", dataCarrito=dataCarrito, total=total)


@app.route("/registro", methods=["GET", "POST"])
def registro():
    database = Database()
    if request.method == "GET":
        data = database.getAllCourse()
        print(data)
        return render_template("registro.html", courses=data)
    else:
        name = request.form["name"]
        contrasenna = request.form["contrasenna"]
        correo = request.form["correo"]
        check = database.checkUser(name)
        if check is True:
            rows = database.insertCourse(name, contrasenna, correo)
            return redirect("/")
        else:
            return render_template(
                "registro.html",
                message="El nombre de usuario que usted ha elegido ya existe, intente nuevamente con otro",
            )


@app.route("/loginform", methods=MethodUtil.list_ALL())
def loginform():
    if request.method == "GET":
        session.pop("id", None)
        session.pop("user", None)
        session.pop("role", None)
        session.pop("nombre", None)
        session.pop("apellido", None)
        session.pop("email", None)
        session.pop("nombre_tarjeta", None)
        session.pop("num_tarjeta", None)
        session.pop("mes_venc", None)
        session.pop("anno_venc", None)
        session.pop("cvv", None)
        session.pop("direccion", None)
        session.pop("ciudad", None)
        session.pop("departamento", None)
        return render_template("login.html", message="")

    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]
        print(password)
        print(generate_password_hash(password))
        print(
            check_password_hash(
                "pbkdf2:sha256:150000$Q5PULnGV$bdc51198ad18432f00fea6a5cb59bec4d7977cb28d3e7ef575bab3b93bfa9628",
                "12345",
            )
        )
        logic = UserLogic()

        userdata = logic.getUserData(user)

        session["id"] = userdata.id
        session["user"] = userdata.user
        session["role"] = userdata.role
        session["nombre"] = userdata.nombre
        session["apellido"] = userdata.apellido
        session["email"] = userdata.email
        session["nombre_tarjeta"] = userdata.nombre_tarjeta
        session["num_tarjeta"] = userdata.num_tarjeta
        session["mes_venc"] = userdata.mes_venc
        session["anno_venc"] = userdata.anno_venc
        session["cvv"] = userdata.cvv
        session["direccion"] = userdata.direccion
        session["ciudad"] = userdata.ciudad
        session["departamento"] = userdata.departamento
        databasePedidos = DatabasePedidos()
        dataprecio = databasePedidos.precioEnvio(session["departamento"])
        session["precio"] = dataprecio[2]
        print(dataprecio[2])
        if userdata is not None:
            if userdata.password == password:
                if userdata.role == "admin":
                    return render_template("index.html", userdata=userdata)
                else:
                    return render_template("index.html", userdata=userdata)
            else:
                return render_template("login.html", message="hubo error")
        else:
            return render_template("login.html", message="hubo error")


@app.route("/logout")
def logout():

    session.pop("id", None)
    session.pop("user", None)
    session.pop("role", None)
    session.pop("nombre", None)
    session.pop("apellido", None)
    session.pop("email", None)
    session.pop("nombre_tarjeta", None)
    session.pop("num_tarjeta", None)
    session.pop("mes_venc", None)
    session.pop("anno_venc", None)
    session.pop("cvv", None)
    session.pop("direccion", None)
    session.pop("ciudad", None)
    session.pop("departamento", None)
    session.pop("precio", None)

    return render_template("index.html")


@app.route("/profile", methods=["GET", "POST"])
def profile():
    database = Database()
    if request.method == "GET":
        return render_template("profile.html")
    else:
        print(request.form)
        name = request.form["nombre"]
        apellido = request.form["apellido"]
        direccion = request.form["direccion"]
        ciudad = request.form["ciudad"]
        departamento = request.form["departamento"]
        nombre_tarjeta = request.form["nombre_tarjeta"]
        num_tarjeta = request.form["num_tarjeta"]
        mes_venc = request.form["mes_venc"]
        anno_venc = request.form["anno_venc"]
        cvv = request.form["cvv"]
        rows = database.updateUser(
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
        )
        session.pop("nombre", None)
        session.pop("apellido", None)
        session.pop("nombre_tarjeta", None)
        session.pop("num_tarjeta", None)
        session.pop("mes_venc", None)
        session.pop("anno_venc", None)
        session.pop("cvv", None)
        session.pop("direccion", None)
        session.pop("ciudad", None)
        session.pop("departamento", None)
        session.pop("precio", None)
        session["nombre"] = name
        session["apellido"] = apellido
        session["nombre_tarjeta"] = nombre_tarjeta
        session["num_tarjeta"] = num_tarjeta
        session["mes_venc"] = mes_venc
        session["anno_venc"] = anno_venc
        session["cvv"] = cvv
        session["direccion"] = direccion
        session["ciudad"] = ciudad
        session["departamento"] = departamento
        databasePedidos = DatabasePedidos()
        dataprecio = databasePedidos.precioEnvio(session["departamento"])
        session["precio"] = dataprecio[2]
        print(f"{rows} rows affected")
        return redirect("/profile")


@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    database = Database()
    if request.method == "GET":
        return render_template("checkout.html")
    else:
        cbox1 = request.form.getlist("cbox1")
        print(cbox1)
        print(request.form)
        if cbox1:
            if cbox1[0] == "checked":
                name = request.form["nombre"]
                apellido = request.form["apellido"]
                direccion = request.form["direccion"]
                ciudad = request.form["ciudad"]
                departamento = request.form["departamento"]
                nombre_tarjeta = request.form["nombre_tarjeta"]
                num_tarjeta = request.form["num_tarjeta"]
                mes_venc = request.form["mes_venc"]
                anno_venc = request.form["anno_venc"]
                cvv = request.form["cvv"]
                rows = database.updateUser(
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
                )
                session.pop("nombre", None)
                session.pop("apellido", None)
                session.pop("nombre_tarjeta", None)
                session.pop("num_tarjeta", None)
                session.pop("mes_venc", None)
                session.pop("anno_venc", None)
                session.pop("cvv", None)
                session.pop("direccion", None)
                session.pop("ciudad", None)
                session.pop("departamento", None)
                session["nombre"] = name
                session["apellido"] = apellido
                session["nombre_tarjeta"] = nombre_tarjeta
                session["num_tarjeta"] = num_tarjeta
                session["mes_venc"] = mes_venc
                session["anno_venc"] = anno_venc
                session["cvv"] = cvv
                session["direccion"] = direccion
                session["ciudad"] = ciudad
                session["departamento"] = departamento
                print(f"{rows} rows affected")
                return redirect("/recibo")
        else:
            return redirect("/recibo")


@app.route("/recibo")
def recibo():
    return render_template("recibo.html")


@app.route("/pedidos")
def pedidos():
    databasePedidos = DatabasePedidos()
    idusuario = session["id"]
    if request.method == "GET":
        dataPedidos = databasePedidos.getAllPedidos(idusuario)
        dataproductos = databasePedidos.getAllProd(idusuario)
        return render_template(
            "pedidos.html", dataPedidos=dataPedidos, dataproductos=dataproductos
        )


if __name__ == "__main__":
    app.run(debug=True)
