from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models import db, User, Product
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password')
    
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists')
            return render_template('signup.html')
        
        user = User(name=name, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        login_user(user)
        return redirect(url_for('home'))
    
    return render_template('signup.html')

@app.route('/home')
@login_required
def home():
    products = Product.query.all()
    return render_template('home.html', products=products)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('welcome'))

def create_tables():
    with app.app_context():
        db.create_all()
        
        if Product.query.count() == 0:
            sample_products = [
                Product(name="Wireless Headphones", price=99.99, description="Premium wireless headphones with noise cancellation", image_url="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=300"),
                Product(name="Smart Watch", price=199.99, description="Advanced fitness tracking smartwatch", image_url="https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=300"),
                Product(name="Laptop Stand", price=49.99, description="Ergonomic aluminum laptop stand", image_url="https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=300"),
                Product(name="Bluetooth Speaker", price=79.99, description="Portable waterproof bluetooth speaker", image_url="https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=300"),
                Product(name="Gaming Mouse", price=59.99, description="High-precision gaming mouse with RGB lighting", image_url="https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=300"),
                Product(name="USB-C Hub", price=39.99, description="Multi-port USB-C hub with HDMI and USB 3.0", image_url="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=300"),
            ]
            
            for product in sample_products:
                db.session.add(product)
            db.session.commit()

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)