from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, Blueprint
from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from rage import mysql, jwt
import smtplib

products = Blueprint('products', __name__)

@products.route('/newProduct', methods=['POST'])
def newProduct():
    if request.method == 'POST':
        print("entra")
        # Obtener campos de la peticion
        precio = request.get_json()['precio']
        tipo = request.get_json()['tipo']
        subtipo = request.get_json()['subtipo']
        nombre = request.get_json()['nombre']

        try:
            cur = mysql.connection.cursor()

            resultado = cur.execute('INSERT INTO producto (precio, tipo, subtipo, nombre) VALUES (%s, %s, %s, %s)',
            (precio, tipo, subtipo, nombre))

            mysql.connection.commit()

            result = "success"
            return result, 200

        except Exception as e:
            print(e)
            return "Error", 409



@products.route('/existProduct', methods=['POST'])
def existProduct():
    if request.method == 'POST':
        print("entra")

        nombre = request.get_json()['nombre']

        try:
            cur = mysql.connection.cursor()

            resultado = cur.execute("SELECT * FROM producto WHERE nombre ='" + str(nombre) + "'") 

            if resultado == 0:
                result = "Error"
            else:
                result = "success"

            mysql.connection.commit()

            
            return result, 200

        except Exception as e:
            print(e)
            return "Error", 409


@products.route('/nameId', methods=['POST'])
def nameId():
    if request.method == 'POST':
        print("entra")

        nombre = request.get_json()['nombre']

        try:
            cur = mysql.connection.cursor()

            resultado = cur.execute("SELECT id FROM producto WHERE nombre ='" + str(nombre) + "'") 

            if resultado == 0:
                return "Error", 404
            
            resultado = cur.fetchone()

            mysql.connection.commit()

            return jsonify(resultado), 200

        except Exception as e:
            print(e)
            return "Error", 409


@products.route('/allProducts', methods=['POST'])
def allProducts():
    if request.method == 'POST':
        print("entra")

        try:
            cur = mysql.connection.cursor()

            resultado = cur.execute("SELECT * FROM producto") 
            if resultado == 0:
                return "Error", 404

            resultado = cur.fetchall()

            mysql.connection.commit()

            return jsonify(resultado), 200

        except Exception as e:
            print(e)
            return "Error", 409


@products.route('/tipeProducts', methods=['POST'])
def tipeProducts():
    if request.method == 'POST':
        print("entra")

        tipo = request.get_json()['tipo']

        try:
            cur = mysql.connection.cursor()

            resultado = cur.execute("SELECT * FROM producto WHERE tipo = '" + str(tipo) + "'") 
            if resultado == 0:
                return "Error", 404

            resultado = cur.fetchall()

            mysql.connection.commit()

            return jsonify(resultado), 200

        except Exception as e:
            print(e)
            return "Error", 409

@products.route('/idProduct', methods=['POST'])
def idProduct():
    if request.method == 'POST':
        print("entra")

        id = request.get_json()['id']

        try:
            cur = mysql.connection.cursor()

            resultado = cur.execute("SELECT * FROM producto WHERE id = '"+ id + "'") 
            if resultado == 0:
                return "Error", 404

            resultado = cur.fetchone()

            mysql.connection.commit()

            return jsonify(resultado), 200

        except Exception as e:
            print(e)
            return "Error", 409




            

        



