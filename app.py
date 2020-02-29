import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# initialize Flask App
app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///' + os.path.join(base_dir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)


# Product Class / Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


# Product Schema
class Product_Schema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'quantity')


# Init Schema
product_schema = Product_Schema()
products_schema = Product_Schema(many=True)


@app.route('/ready', methods=['GET'])
def ready():
    return jsonify(
        {
            'ready': 'ready call initialized'
        }
    )


# Create a product
@app.route('/product', methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    quantity = request.json['quantity']

    new_product = Product(name, description, price, quantity)
    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
