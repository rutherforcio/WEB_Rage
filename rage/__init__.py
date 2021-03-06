from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
# from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
#from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt)


app = Flask(__name__)


mysql = MySQL()
#bcrypt = Bcrypt()
jwt = JWTManager()


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'rage'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['JWT_SECRET_KEY'] = 'secret'

mysql.init_app(app)
#bcrypt.init_app(app)
jwt.init_app(app)

#from baitu.ficherosPython.ventas import ventas
#from baitu.ficherosPython.usuarios import users

#app.register_blueprint(ventas)
#app.register_blueprint(users)

from rage.code.pedidos import pedidos
from rage.code.users import users
from rage.code.products import products
from rage.code.carrito import carrito

app.register_blueprint(pedidos)
app.register_blueprint(users)
app.register_blueprint(products)
app.register_blueprint(carrito)



cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def create_app():
    global app
    return app
