import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# initialize Flask App
app = Flask(__name__)
base_dir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
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
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'quantity')


# Init Schema
product_schema = ProductSchema()
all_products_schema = ProductSchema(many=True)


# Ready call
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

# Get all Products
@app.route('/products', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = all_products_schema.dump(all_products)
    return jsonify(result)

# Get Single Products by id
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)

# Update a product
@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    quantity = request.json['quantity']

    product.name = name
    product.description = description
    product.price = price
    product.quantity = quantity

    db.session.commit()

    return product_schema.jsonify(product)

# Delete a product
@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    return product_schema.jsonify(product)


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
