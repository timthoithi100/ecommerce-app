from app import app, db
from models import User, Product

def init_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("Database tables created!")

def add_sample_data():
    with app.app_context():
        sample_products = [
            Product(name="Wireless Headphones", price=99.99, description="Premium wireless headphones with noise cancellation", image_url="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=300"),
            Product(name="Smart Watch", price=199.99, description="Advanced fitness tracking smartwatch", image_url="https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=300"),
            Product(name="Laptop Stand", price=49.99, description="Ergonomic aluminum laptop stand", image_url="https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=300"),
            Product(name="Bluetooth Speaker", price=79.99, description="Portable waterproof bluetooth speaker", image_url="https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=300"),
            Product(name="Gaming Mouse", price=59.99, description="High-precision gaming mouse with RGB lighting", image_url="https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=300"),
            Product(name="USB-C Hub", price=39.99, description="Multi-port USB-C hub with HDMI and USB 3.0", image_url="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=300"),
            Product(name="Mechanical Keyboard", price=129.99, description="Premium mechanical keyboard with blue switches", image_url="https://images.unsplash.com/photo-1541140532154-b024d705b90a?w=300"),
            Product(name="Monitor Stand", price=79.99, description="Adjustable monitor stand with cable management", image_url="https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=300"),
        ]
        
        for product in sample_products:
            db.session.add(product)
        
        admin_user = User(name="Admin User", email="admin@shophub.com")
        admin_user.set_password("admin123")
        db.session.add(admin_user)
        
        db.session.commit()
        print("Sample data added!")

if __name__ == "__main__":
    init_db()
    add_sample_data()