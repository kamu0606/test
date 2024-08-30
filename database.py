# prompt: create a sample program of database using python

import sqlite3

# Connect to database (creates it if it doesn't exist)
conn = sqlite3.connect('mydatabase.db')

# Create a cursor
cursor = conn.cursor()

# Create a table
cursor.execute('''
  CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    department TEXT NOT NULL
  )
''')

# Insert data into table
cursor.execute("INSERT INTO employees VALUES (1, 'John Doe', 'Sales')")
cursor.execute("INSERT INTO employees VALUES (2, 'Jane Smith', 'Marketing')")

# Commit changes
conn.commit()

# Retrieve data from table
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

# Print the rows
for row in rows:
  print(row)

# Close the connection
conn.close()
