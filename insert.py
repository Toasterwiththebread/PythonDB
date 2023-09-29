def one(database_collection, database_name, data):
    file = open(database_collection + "/" + database_name + ".json", "a")
    file.write(data + "\n")
    file.close()
    return True