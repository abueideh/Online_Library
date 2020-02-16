from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import urllib.parse

catalog = Flask(__name__)

catalog.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Books.db'

db = SQLAlchemy(catalog)

ma = Marshmallow(catalog)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(200))
    quantity = db.Column(db.Integer)
    name = db.Column(db.String(200))
    price = db.Column(db.Integer)
    
class BookSchema_search(ma.Schema):
    class Meta:
        fields = ('id','topic','name')
books_schema_search = BookSchema_search(many = True)

class BookSchema_lookup(ma.Schema):
    class Meta:
        fields = ('id','quantity','price')
book_schema_lookup = BookSchema_lookup()


@catalog.route('/search/<subject>' ,methods=['POST','GET'])
def search(subject):
    urllib.parse.unquote(subject)
    all_books = Book.query.filter(Book.topic== subject)
    result = books_schema_search.dump(all_books)
    return jsonify(result)


@catalog.route('/lookup/<id>' ,methods=['POST','GET'])
def lookup(id):
    my_book = Book.query.get(id)
    return book_schema_lookup.jsonify(my_book)

@catalog.route('/quantity/<id>' ,methods=['POST','GET'])
def get_quantity(id):
    my_book = Book.query.get(id)
    return str(my_book.quantity)

@catalog.route('/update/<id>' ,methods=['POST','GET'])
def decrement(id):
    my_book = Book.query.get(id)
    my_book.quantity = my_book.quantity-1
    db.session.commit()
    return str("book.quantity")


if __name__ == "__main__":
    catalog.run(host='192.168.1.101')
    catalog.run(debug=True)
