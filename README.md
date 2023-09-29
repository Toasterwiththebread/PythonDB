# PythonDB

## Description

This project is a Python library for working with databases, providing functionalities for creating, deleting, checking, as well as CRUD (Create, Read, Update, Delete) operations on database collections.

## Installation

To use this library, you can just download it and drag it into where you will be using it

## Usage

```
import database_handler

# Create a new database
result = database_handler.createDatabase(database_collection, database_name)

# Delete a database
result = database_handler.deleteDatabase(database_collection, database_name)

# Check if a database exists
result = database_handler.checkDatabase(database_collection, database_name)

# Delete a document from a database collection
result = database_handler.deleteOne(database_collection, database_name, data)

# Find a document in a database collection
result = database_handler.findOne(database_collection, database_name, data)

# Insert a document into a database collection
result = database_handler.insertOne(database_collection, database_name, data)

# Update a document in a database collection
result = database_handler.updateOne(database_collection, database_name, old_data, new_data)
```

Make sure your new data includes the whole string to update, or else it will just replace the whole string

Made this for a shitty YouTube video lol
