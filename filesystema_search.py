# Now that absolute paths are shown, we can inspect them for file metadata

import os
from os.path import abspath, join, getsize
import sqlite3

connection = sqlite3.connect('file_system.db')  # crear conección al database

# table = 'CREATE TABLE files (id integer primary key, path TEXT, size INTEGER)'   
cursor = connection.cursor()    # El cursor es para poder hacer el commit
# cursor.execute(table)           # Execute the query
# connection.commit()             # Para hacer los cambios en un commit

# file_metadata = {}
# for root, directories, files in os.walk('.'):
#     for _file in files:
#         full_path = os.path.join(root, _file)
#         size = os.path.getsize(full_path)
#         file_metadata[full_path] = size



# for path, size in file_metadata.items():
#     query = 'INSERT INTO files(path, size) VALUES(?, ?)'
#     # the execute() method accepts a query and optionally a tuple with values 
#     # corresponding to the question marks in VALUES
#     cursor.execute(query, (path, size))
#     connection.commit()


query = 'SELECT * from files WHERE size>1000 LIMIT 10'
for i in cursor.execute(query):
    print(i)


