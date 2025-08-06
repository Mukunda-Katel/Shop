#!/usr/bin/env python3
"""
Setup script for ShoppingMart Django project.
This script helps initialize the project with sample data.
"""

import os
import sys
import django
from decimal import Decimal

# Add the project directory to the Python path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_dir)

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopping_mart.settings')
django.setup()

from django.contrib.auth.models import User
from products.models import Category, Product
from accounts.models import Profile

def create_sample_data():
    """Create sample data for the project"""
    print("Creating sample data...")
    
    # Create categories
    categories = [
        {'name': 'Electronics', 'description': 'Phones, laptops, and other electronic devices'},
        {'name': 'Clothing', 'description': 'Fashion and apparel for all ages'},
        {'name': 'Books', 'description': 'Books, ebooks, and educational materials'},
        {'name': 'Home & Garden', 'description': 'Home decor, furniture, and gardening supplies'},
        {'name': 'Sports', 'description': 'Sports equipment and fitness gear'},
    ]
    
    for cat_data in categories:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={'description': cat_data['description']}
        )
        if created:
            print(f"Created category: {category.name}")
    
    # Create a sample user (seller)
    if not User.objects.filter(username='demo_seller').exists():
        demo_user = User.objects.create_user(
            username='demo_seller',
            email='demo@example.com',
            password='demopass123',
            first_name='Demo',
            last_name='Seller'
        )
        print("Created demo seller account")
        
        # Create sample products
        electronics = Category.objects.get(name='Electronics')
        clothing = Category.objects.get(name='Clothing')
        books = Category.objects.get(name='Books')
        
        sample_products = [
            {
                'name': 'iPhone 14 Pro',
                'description': 'Latest iPhone with amazing camera and performance.',
                'price': Decimal('999.99'),
                'category': electronics,
                'stock': 50,
                'seller': demo_user,
            },
            {
                'name': 'Samsung Galaxy S23',
                'description': 'Powerful Android smartphone with excellent display.',
                'price': Decimal('799.99'),
                'category': electronics,
                'stock': 30,
                'seller': demo_user,
            },
            {
                'name': 'Casual T-Shirt',
                'description': 'Comfortable cotton t-shirt for everyday wear.',
                'price': Decimal('19.99'),
                'category': clothing,
                'stock': 100,
                'seller': demo_user,
            },
            {
                'name': 'Python Programming Book',
                'description': 'Learn Python programming from scratch.',
                'price': Decimal('39.99'),
                'category': books,
                'stock': 25,
                'seller': demo_user,
            }
        ]
        
        for product_data in sample_products:
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults=product_data
            )
            if created:
                print(f"Created product: {product.name}")

def main():
    """Main setup function"""
    print("ShoppingMart Setup Script")
    print("=" * 40)
    
    try:
        create_sample_data()
        print("\n✅ Setup completed successfully!")
        print("\nNext steps:")
        print("1. Run: python manage.py makemigrations")
        print("2. Run: python manage.py migrate")
        print("3. Run: python manage.py createsuperuser")
        print("4. Run: python manage.py runserver")
        print("\nDemo seller credentials:")
        print("Username: demo_seller")
        print("Password: demopass123")
        
    except Exception as e:
        print(f"❌ Setup failed: {e}")
        return 1
    
    return 0

if __name__ == '__main__':
    sys.exit(main())
