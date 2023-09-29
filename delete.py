import os

def one(database_collection, database_name, data):
    file = open(database_collection + "/" + database_name + ".json", "r+")

    temp_data_array = []

    for line_number, line_data in enumerate(file):
        if data not in line_data:
            temp_data_array.append(line_data)

    file.close()

    os.remove(database_collection + "/" + database_name + ".json")

    file = open(database_collection + "/" + database_name + ".json", "a")

    for line_data in temp_data_array:
        file.write(line_data + "\n")

    file.close()

    return True