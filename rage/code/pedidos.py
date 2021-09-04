from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, Blueprint
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
from flask_jwt_extended import JWTManager
from rage import mysql, jwt
import smtplib

pedidos = Blueprint('pedidos', __name__)

@pedidos.route('/anyadir', methods=['POST'])
@cross_origin()
def anyadir():
    if request.method == 'POST':
        print("entra pedido")
        # Obtener campos de la peticion
        id_usuario = request.get_json()['id_usuario']
        id_producto = request.get_json()['id_producto']
        cantidad = request.get_json()['cantidad']

        print(id_usuario)
        print(id_producto)
        print(cantidad)
        try:
            cur = mysql.connection.cursor()

            cur.execute('INSERT INTO pedido (id_usuario, id_producto, n_pedido, cantidad) VALUES (%s, %s, %s, %s)',
            (id_usuario, id_producto, 1, cantidad))

            mysql.connection.commit()

            #access_token = create_access_token(identity = {'login': Login,'nombre': Nombre,'apellidos': Apellidos, 'email': Email, 'foto': Foto})
            #result = access_token
            result = "success"
            return result, 200

        except Exception as e:
            print(e)
            return "Error", 409

