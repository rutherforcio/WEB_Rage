from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, Blueprint
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
from flask_jwt_extended import JWTManager
from rage import mysql, jwt
import smtplib
import json
import random

pedidos = Blueprint('pedidos', __name__)

@pedidos.route('/anyadir', methods=['POST'])
@cross_origin()
def anyadir():
    if request.method == 'POST':
        # Obtener campos de la peticion
        id_usuario = request.get_json()['id_usuario']
        productos = request.get_json()['productos']

        try:
            # Generar numero de pedido aleatorio unico
            done = False
            r = 0
            while not done:
                r = random.randrange(0, 10000)
                cur = mysql.connection.cursor()
                exists = cur.execute("SELECT * FROM pedido WHERE n_pedido =" + str(r) + "")

                if exists == 0:
                    done = True
            
            n_pedido = r

            # Insertar pedidos
            for producto in productos:
                cur = mysql.connection.cursor()

                cur.execute('INSERT INTO pedido (id_usuario, id_producto, n_pedido, cantidad) VALUES (%s, %s, %s, %s)',
                (id_usuario, producto['id_producto'], n_pedido, producto['cantidad']))

                mysql.connection.commit()


            result = "success"
            return result, 200

        except Exception as e:
            print(e)
            return "Error", 409

