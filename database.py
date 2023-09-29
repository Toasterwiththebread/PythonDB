import os

def create(database_collection, database_name):
    try:
        file = open(database_collection + "/" + database_name + ".json", "a")
        file.close()
        return True
    except:
        os.mkdir(database_collection)
        file = open(database_collection + "/" + database_name + ".json", "a")
        file.close()
        return True
    
def delete(database_collection, database_name):
    os.remove(database_collection + "/" + database_name + ".json")

def check(database_collection, database_name):
    try:
        file = open(database_collection + "/" + database_name + ".json", "a")
        file.close()
        return True
    except:
        return False