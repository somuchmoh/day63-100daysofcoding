from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy()
db.init_app(app)
app.secret_key = 'Your_Ssecret_Key'
Bootstrap5(app)
choices = [1, 2, 3, 4, 5]


class LibForm(FlaskForm):
    book_name = StringField('Name', validators=[DataRequired(), Length(min=4)])
    book_author = StringField('Author', validators=[DataRequired(), Length(min=6)])
    book_rating = SelectField('Rating', choices=choices, validators=[DataRequired()])
    submit = SubmitField('Submit')


class RateForm(FlaskForm):
    rating = SelectField('Rating', choices=choices, validators=[DataRequired()])
    submit = SubmitField('Change Rating')


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = LibForm()
    if form.validate_on_submit():
        new_book = Book(title=form.data['book_name'], author=form.data['book_author'], rating=form.data['book_rating'])
        db.session.add(new_book)
        db.session.commit()
        return redirect("/")
    return render_template('add.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)

