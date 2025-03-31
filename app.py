from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure SQLite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define Product Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

# Ensure the database is created
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

# API to get products
@app.route('/get_products', methods=['GET'])
def get_products():
    products = Product.query.all()
    product_list = [{'id': p.id, 'name': p.name, 'quantity': p.quantity, 'price': p.price} for p in products]
    return jsonify({'products': product_list})

# API to add product
@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.json
    new_product = Product(name=data['name'], quantity=data['quantity'], price=data['price'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({'message': 'Product added successfully'})

# API to edit product
@app.route('/edit_product/<int:product_id>', methods=['PUT'])
def edit_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    data = request.json
    product.name = data['name']
    product.quantity = data['quantity']
    product.price = data['price']
    db.session.commit()
    return jsonify({'message': 'Product updated successfully'})

# API to delete product
@app.route('/delete_product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    db.session.delete(product)
    db.session.commit()
    return jsonify({'message': 'Product deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
