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


@users.route('/getUser', methods=['POST'])
def getUser():
    if request.method == 'POST':
        correo = request.get_json()['correo']
        
        try:
            cur = mysql.connection.cursor()

            result = cur.execute("SELECT * FROM usuario WHERE correo ='" + str(correo) + "'")

            if result == 0:
                return "Error", 404

            resultado = cur.fetchone()

            mysql.connection.commit()

            return jsonify(resultado), 200

        except Exception as e:
            print(e)
            return "Error", 409


@users.route('/setDireccion', methods=['POST'])
def setDireccion():
    if request.method == 'POST':
        correo = request.get_json()['correo']
        direcionentrega = request.get_json()['direcionentrega']
        
        try:
            cur = mysql.connection.cursor()

            cur.execute("UPDATE usuario SET direcionEntrega ='" + str(direcionentrega) + "'  WHERE correo ='" + str(correo) + "'")

            mysql.connection.commit()
            result = "success"

            return result, 200

        except Exception as e:
            print(e)
            return "Error", 409


@users.route('/setPago', methods=['POST'])
def setPago():
    if request.method == 'POST':
        correo = request.get_json()['correo']
        formapago = request.get_json()['formapago']
        
        try:
            cur = mysql.connection.cursor()

            if formapago != "Paypal" and formapago != "Transferencia":
                result = "Error"
            else:
                
                cur.execute("UPDATE usuario SET formapago ='" + str(formapago) + "'  WHERE correo ='" + str(correo) + "'")
                mysql.connection.commit()
                result = "success"

            return result, 200

        except Exception as e:
            print(e)
            return "Error", 409


@users.route('/newPassword', methods=['POST'])
def newPassword():
    if request.method == 'POST':
        
        newcontrasenya = request.get_json()['newcontrasenya']
        verifycontrasenya = request.get_json()['verifycontrasenya']
        correo = request.get_json()['correo']
        
        try:
            cur = mysql.connection.cursor()
            cur.execute("SELECT contrasenya FROM usuario WHERE correo ='" + str(correo) + "'")
            userContrasenya = cur.fetchone()
            contrasenya = (userContrasenya['contrasenya'])
            if contrasenya == verifycontrasenya:
                cur.execute("UPDATE usuario SET contrasenya ='" + str(newcontrasenya) + "'  WHERE correo ='" + str(correo) + "'")
                result = "success"
            else:
                
                result = "Error"

            mysql.connection.commit()
            
            return result, 200

        except Exception as e:
            print(e)
            return "Error", 409

@users.route('/newCorreo', methods=['POST'])
def newCorreo():
    if request.method == 'POST':
        
        newcorreo = request.get_json()['newcorreo']
        verifycontrasenya = request.get_json()['verifycontrasenya']
        correo = request.get_json()['correo']
        
        try:
            cur = mysql.connection.cursor()
            cur.execute("SELECT contrasenya FROM usuario WHERE correo ='" + str(correo) + "'")
            userContrasenya = cur.fetchone()
            contrasenya = (userContrasenya['contrasenya'])
            if contrasenya == verifycontrasenya:
                cur.execute("UPDATE usuario SET correo ='" + str(newcorreo) + "'  WHERE correo ='" + str(correo) + "'")
                result = "success"
            else:
                
                result = "Error"

            mysql.connection.commit()
            
            return result, 200

        except Exception as e:
            print(e)
            return "Error", 409
