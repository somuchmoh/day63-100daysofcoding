import sqlite3

# Create a connection to a new database
db = sqlite3.connect("books-collection.db")

# We need to create a cursor which will control our database.
cursor = db.cursor()

# Our database can contain many tables. Add this code below all the previous lines.

# cursor.execute("CREATE TABLE books "
#                "(id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")


# To add data to our table we can head back to main.py and write the following code:
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()