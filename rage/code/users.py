from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, Blueprint
from flask_mysqldb import MySQL
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from rage import mysql, jwt
import smtplib

users = Blueprint('users', __name__)

@users.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        print("entra")
        # Obtener campos de la peticion
        password = request.get_json()['password']
        nombre = request.get_json()['nombre']
        correo = request.get_json()['correo']

        try:
            cur = mysql.connection.cursor()

            resultado = cur.execute('INSERT INTO usuario (correo, nombre, contrasenya, direcionEntrega, formaPago) VALUES (%s, %s, %s, %s, %s)',
            (correo, nombre, password, '', ''))

            mysql.connection.commit()

            #access_token = create_access_token(identity = {'login': Login,'nombre': Nombre,'apellidos': Apellidos, 'email': Email, 'foto': Foto})
            #result = access_token
            result = "success"
            return result, 200

        except Exception as e:
            print(e)
            return "Error", 409