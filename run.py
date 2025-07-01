from app import app, db
from models import User, Product

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if Product.query.count() == 0:
            from database import add_sample_data
            add_sample_data()
    
    print("Starting ShopHub E-commerce Application...")
    print("Visit: http://127.0.0.1:5000")
    print("Admin credentials: admin@shophub.com / admin123")
    app.run(debug=True, host='0.0.0.0', port=5000)