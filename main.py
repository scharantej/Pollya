
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True)
    author = db.Column(db.String(80))

db.create_all()

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    books = Book.query.filter(Book.title.like('%' + query + '%')).all()
    return render_template('index.html', books=books)

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form.get('title')
    author = request.form.get('author')
    book = Book(title=title, author=author)
    db.session.add(book)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/remove_book', methods=['POST'])
def remove_book():
    id = request.form.get('id')
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
