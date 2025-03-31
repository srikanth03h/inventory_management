from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/add', methods=['POST'])
def add_product():
    name = request.form['name']
    quantity = int(request.form['quantity'])
    price = float(request.form['price'])
    
    new_product = Product(name=name, quantity=quantity, price=price)
    db.session.add(new_product)
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_product(id):
    product = Product.query.get(id)
    if product:
        db.session.delete(product)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['POST'])
def edit_product(id):
    product = Product.query.get(id)
    if product:
        product.name = request.form['name']
        product.quantity = int(request.form['quantity'])
        product.price = float(request.form['price'])
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
