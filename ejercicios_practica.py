#!/usr/bin/env python
'''
SQL Introducción [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Sebastian Volpe"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import json

import tinymongo as tm
import tinydb

# Bug: https://github.com/schapman1974/tinymongo/issues/58
class TinyMongoClient(tm.TinyMongoClient):
    @property
    def _storage(self):
        return tinydb.storages.JSONStorage

db_name = 'secundaria'


def clear():
    conn = TinyMongoClient()
    db = conn[db_name]

    # Eliminar todos los documentos que existan en la coleccion estudiante
    db.estudiante.remove({})

    # Cerrar la conexión con la base de datos
    conn.close()

def insert_persona(name, age, grade, tutor):
    conn = TinyMongoClient()
    db = conn[db_name]

    persona_json = {"name": name, "age": age, "grade": grade, "tutor":tutor}
    db.estudiante.insert_one(persona_json)

    conn.close()



def fill():
    print('Completemos esta tablita!')
    # Llenar la coleccion "estudiante" con al menos 5 estudiantes
    # Cada estudiante tiene los posibles campos:
    # id --> este campo es auto completado por mongo
    # name --> El nombre del estudiante (puede ser solo nombre sin apellido)
    # age --> cuantos años tiene el estudiante
    # grade --> en que año de la secundaria se encuentra (1-6)
    # tutor --> nombre de su tutor

    # Se debe utilizar la sentencia insert_one o insert_many.
    insert_persona("Julio", 22, 2, "Carlos")
    insert_persona("juan", 23, 1, "Carlos")
    insert_persona("Martin", 24, 3, "Jose")
    insert_persona("Florencia", 22, 3, "Jose")
    insert_persona("Soledad", 21, 2, "Maria")

def show():
    print('Comprobemos su contenido, ¿qué hay en la tabla?')
    # Utilizar la sentencia find para imprimir en pantalla
    # todos los documentos de la DB
    # Queda a su criterio serializar o no el JSON "dumps"
    #  para imprimirlo en un formato más "agradable"

    conn = TinyMongoClient()
    db = conn[db_name]


    cursor = db.estudiante.find()
    data = list(cursor)
    doc = json.dumps(data, indent=4)
    print(doc)

    conn.close()

def find_by_grade(grado):
    print('Operación búsqueda!')
    # Utilizar la sentencia find para imprimir en pantalla
    # aquellos estudiantes que se encuentra en en año "grade"

    # De la lista de esos estudiantes debe imprimir
    # en pantalla unicamente los siguiente campos por cada uno:
    # id / name / age

    conn = TinyMongoClient()
    
    db = conn[db_name]
    person_data = db.estudiante.find({"grade": grado})
    data = list(person_data)
    
    for i in data:
        print("Nombre",i["name"], "Edad",i["age"],"Id",i["_id"])

    conn.close()
    return person_data

def insert(student):
    print('Nuevos ingresos!')
    # Utilizar la sentencia insert_one para ingresar nuevos estudiantes
    # a la secundaria

    # El parámetro student deberá ser un JSON el cual se inserta en la db
    conn = TinyMongoClient()
    db = conn[db_name]

    db.estudiante.insert_one(student)

    conn.close()


def count(grado):
    print('Contar estudiantes')
    # Utilizar la sentencia find + count para contar
    # cuantos estudiantes pertenecen el grado "grade"
    # Conectarse a la base de datos

    conn = TinyMongoClient()
    db = conn[db_name]

    count = db.estudiante.find({"grade": grado}).count()

    conn.close()
    return count

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # Borrar la db
    clear()

    fill()
    show()

    grade = 2
    find_by_grade(grade)

    student = {"name": "Sebas", "age": 22, "grade": 3, "tutor":"Julio"}
    insert(student)
    
    count(3)

