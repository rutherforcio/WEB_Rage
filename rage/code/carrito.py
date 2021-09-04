from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, Blueprint
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
from flask_jwt_extended import JWTManager
from rage import mysql, jwt
import smtplib
import json
import random

carrito = Blueprint('carrito', __name__)

@carrito.route('/anyadir_carrito', methods=['POST'])
@cross_origin()
def anyadir_carrito():
    if request.method == 'POST':
        # Obtener campos de la peticion
        id_usuario = request.get_json()['id_usuario']
        productos = request.get_json()['productos']

        try:

            # Insertar elementos
            for producto in productos:
                cur = mysql.connection.cursor()

                cur.execute('INSERT INTO carrito (id_usuario, id_producto, cantidad) VALUES (%s, %s, %s)',
                (id_usuario, producto['id_producto'], producto['cantidad']))

                mysql.connection.commit()


            result = "success"
            return result, 200

        except Exception as e:
            print(e)
            return "Error", 409

@carrito.route('/quitar_carrito', methods=['POST'])
@cross_origin()
def quitar_carrito():
    if request.method == 'POST':

        id_producto = request.get_json()['id_producto']
        id_usuario = request.get_json()['id_usuario'] 

        try:
            cur = mysql.connection.cursor()
            verificacion = cur.execute("SELECT * FROM carrito WHERE id_producto =" + str(id_producto) +" AND id_usuario ='" + str(id_usuario) +"'")
            print(verificacion)
            mysql.connection.commit()
            if verificacion == 1:
                print ("entra")
                cur = mysql.connection.cursor()
                prueba = cur.execute("DELETE FROM carrito WHERE id_producto =" + str(id_producto) +" AND id_usuario ='" + str(id_usuario) +"'")
                mysql.connection.commit()
                #prueba = cur.execute("DELETE FROM carrito WHERE id_producto =" + str(id_producto) +" AND id_usuario ='" + str(id_usuario) +"'")
                if prueba == 1:
                    ("bien")
                else:
                    print("mal")


            else:
                result = "No existe un usario con este producto en el carrito"
                return result, 404


            result = "success"
            return result, 200



        except Exception as e:
            print(e)
            return "Error", 409 

@carrito.route('/listar_carrito', methods=['POST'])
@cross_origin()
def listar_carrito():
    if request.method == 'POST':
        print("entra")
        id_usuario = request.get_json()['id_usuario']

        try:
            cur = mysql.connection.cursor()

            resultado = cur.execute("SELECT * FROM carrito WHERE id_usuario = '" + str(id_usuario) +"'") 
            if resultado == 0:
                return "Error", 404

            resultado = cur.fetchall()

            mysql.connection.commit()

            return jsonify(resultado), 200

        except Exception as e:
            print(e)
            return "Error", 409   