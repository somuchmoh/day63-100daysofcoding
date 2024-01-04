from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Create a database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

# Create a connection
db = SQLAlchemy()
# Initialise the app
db.init_app(app)

# Create a new table
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()

with app.app_context():
    new_book = Book(id=4, title="Anxsqefdiou People", author="Fredrfergrk Backman", rating=9.3)
    db.session.add(new_book)
    db.session.commit()
