# wsgi.py
from flask import Flask, jsonify, abort
app = Flask(__name__)

PRODUCTS = [
        { 'id': 1, 'name': 'Skello' },
        { 'id': 2, 'name': 'Socialive.tv' },
        { 'id': 3, 'name': 'Me' }
    ]
print('list')
print(PRODUCTS)
@app.route('/')
def hello():
    return "Hello World! You're the best"

@app.route('/api/v1/products')
def get_products():
    print('len')
    return jsonify(PRODUCTS), 200

@app.route('/api/v1/products/<int:id>', methods=["GET"])
def get_product(id):
    for product in PRODUCTS:
        if product["id"] == id :
            return jsonify(product)
    return '', 404

@app.route('/api/v1/products/<int:id>', methods=["DELETE"])
def delete_product(id):
    for product in PRODUCTS:
        if product["id"] == id :
            print('delete')
            PRODUCTS.remove(product)
            return '', 204
    return '', 404

@app.route('/api/v1/products', methods=["POST"])
def add_products():
    PRODUCTS.append({"id": 4 ,"name" : "Here"})
    return '', 201

