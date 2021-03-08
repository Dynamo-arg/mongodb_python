#!/usr/bin/env python

__author__ = "Sebastian Volpe"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import json
import requests
import tinymongo as tm
import tinydb

# Bug: https://github.com/schapman1974/tinymongo/issues/58
class TinyMongoClient(tm.TinyMongoClient):
    @property
    def _storage(self):
        return tinydb.storages.JSONStorage

db_name = 'prueba'


def clear():
    conn = TinyMongoClient()
    db = conn[db_name]
    db.todos.remove({})
    conn.close()

def fill():
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    diccionario = response.json()

    conn = TinyMongoClient()
    db = conn[db_name]

    db.todos.insert_many(diccionario)
    conn.close()

def title_completed_count(userId):
    conn = TinyMongoClient()
    db = conn[db_name]

    count = db.persons.find({"nationality": country}).count()
    if userId == db.todos.find({"userId"}):
        print("OK")

    count = db.persons.find({"nationality": country}).count()


    conn.close()
    return userId


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

def insert_persona(name, age, grade, tutor):
    conn = TinyMongoClient()
    db = conn[db_name]

    persona_json = {"name": name, "age": age, "grade": grade, "tutor":tutor}
    db.estudiante.insert_one(persona_json)

    conn.close()




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

if __name__ == "__main__":
    # Borrar DB
    clear()

    fill()

    # Buscar autor
    userId = 5
    title_completed_count(userId)

