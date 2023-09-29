import database

import delete
import find
import insert
import update

def createDatabase(database_collection, database_name):
    result = database.create(database_collection, database_name)
    return result

def deleteDatabase(database_collection, database_name):
    result = database.delete(database_collection, database_name)
    return result

def checkDatabase(database_collection, database_name):
    result = database.check(database_collection, database_name)
    return result

def deleteOne(database_collection, database_name, data):
    result = delete.one(database_collection, database_name, data)
    return result

def findOne(database_collection, database_name, data):
    result = find.one(database_collection, database_name, data)
    return result

def insertOne(database_collection, database_name, data):
    result = insert.one(database_collection, database_name, data)
    return result

def updateOne(database_collection, database_name, old_data, new_data):
    result = update.one(database_collection, database_name, old_data, new_data)
    return result