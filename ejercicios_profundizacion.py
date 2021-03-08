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

    count = db.todos.find({"userId": userId})
    total = 0

    for i in count:
        if i["completed"] == True:
            total += 1
      
    conn.close()
    return total




if __name__ == "__main__":
    
    clear()

    fill()

    userId = 5
    total = title_completed_count(userId)
    print("Cantidad de completados de este usuario:",userId, "Total:",total)

