# PythonDB

## Description

This project is a Python library for working with databases, providing functionalities for creating, deleting, checking, as well as CRUD (Create, Read, Update, Delete) operations on database collections.

## Installation

To use this library, you can just download it and drag it into where you will be using it

## Usage

```
import database
import delete
import find
import insert
import update

# Create a new database
result = createDatabase(database_collection, database_name)

# Delete a database
result = deleteDatabase(database_collection, database_name)

# Check if a database exists
result = checkDatabase(database_collection, database_name)

# Delete a document from a database collection
result = deleteOne(database_collection, database_name, data)

# Find a document in a database collection
result = findOne(database_collection, database_name, data)

# Insert a document into a database collection
result = insertOne(database_collection, database_name, data)

# Update a document in a database collection
result = updateOne(database_collection, database_name, old_data, new_data)
```

Make sure your new data includes the whole string to update, or else it will just replace the whole string

Made this for a shitty YouTube video lol
