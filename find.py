def one(database_collection, database_name, data):
    file = open(database_collection + "/" + database_name + ".json", "r")
    for line_number, line_data in enumerate(file):
        if data in line_data:
            break

    file.close()

    return line_data