# ShoppingMart - Django E-commerce & Social Platform

A beginner-friendly Django web application that combines e-commerce functionality with social features. Perfect for learning Django, CRUD operations, user authentication, real-time chat, and modern web development practices.

## 🚀 Features

### 1. User Authentication & Profiles
- ✅ User registration, login, and logout
- ✅ User profile pages with customizable information
- ✅ Profile picture uploads with automatic resizing
- ✅ Password reset functionality
- ✅ Update profile and change password

### 2. Product Management (CRUD Operations)
- ✅ Create, Read, Update, Delete products
- ✅ Product categories and search functionality
- ✅ Image uploads for products
- ✅ Stock management
- ✅ Product seller information

### 3. Review & Comment System
- ✅ Users can review products with ratings (1-5 stars)
- ✅ Comment on reviews
- ✅ Like/unlike products, reviews, and comments
- ✅ Image uploads for reviews

### 4. Real-Time Chat (Django Channels)
- ✅ Real-time chat rooms for community interaction
- ✅ Private messaging between users
- ✅ Image sharing in chat
- ✅ WebSocket support for instant messaging

### 5. Shopping Cart & Orders
- ✅ Add products to cart
- ✅ Order management system
- ✅ Order tracking with status updates

### 6. Search & Filtering
- ✅ Search products by name, description, or seller
- ✅ Filter by categories
- ✅ Pagination for better performance

### 7. Admin Dashboard
- ✅ Comprehensive admin interface
- ✅ Manage users, products, categories, and orders
- ✅ Analytics and reporting

### 8. Responsive Design
- ✅ Bootstrap 5 for modern, mobile-friendly design
- ✅ Font Awesome icons
- ✅ Custom CSS for enhanced UX

## 🛠 Technology Stack

- **Backend:** Django 4.2.7
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5
- **Database:** SQLite (easily upgradeable to PostgreSQL)
- **Real-time:** Django Channels with Redis
- **Media Handling:** Pillow for image processing
- **Forms:** Django Crispy Forms with Bootstrap

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (optional, for cloning)

## 🚀 Quick Start

### 1. Clone or Download the Project
```bash
git clone <repository-url>
cd Estore
```

### 2. Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser
```bash
python manage.py createsuperuser
```

### 6. Load Sample Data (Optional)
```bash
python setup.py
```

### 7. Run the Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to access the application.

## 📁 Project Structure

```
Estore/
├── shopping_mart/          # Main project settings
├── accounts/               # User authentication & profiles
├── products/              # Product management
├── reviews/               # Product reviews & comments
├── chat/                  # Real-time chat functionality
├── cart/                  # Shopping cart & orders
├── templates/             # HTML templates
├── static/                # CSS, JS, images
├── media/                 # User uploaded files
├── requirements.txt       # Python dependencies
├── setup.py              # Sample data setup script
└── README.md             # This file
```

## 🎯 Learning Objectives

This project is designed to teach:

1. **Django Fundamentals**
   - Models, Views, Templates (MVT)
   - URL routing and namespacing
   - Forms and form validation
   - User authentication system

2. **Database Operations**
   - Model relationships (OneToOne, ForeignKey, ManyToMany)
   - Database migrations
   - QuerySet operations and optimization

3. **File Handling**
   - Image uploads and processing
   - Static files management
   - Media files serving

4. **Real-time Features**
   - WebSockets with Django Channels
   - Redis for channel layers
   - Asynchronous consumers

5. **Frontend Integration**
   - Template inheritance
   - Bootstrap for responsive design
   - AJAX for dynamic interactions
   - JavaScript for enhanced UX

6. **Security Best Practices**
   - CSRF protection
   - User permissions and authentication
   - Secure file uploads
   - Input validation

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root (optional):
```
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
REDIS_URL=redis://localhost:6379
```

### Redis Setup (for Chat)
Install Redis for real-time chat functionality:

**Windows:**
Download and install Redis from the official website

**macOS:**
```bash
brew install redis
redis-server
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install redis-server
```

## 📚 API Endpoints

### Products
- `GET /` - Home page
- `GET /products/` - Product list
- `GET /products/<id>/` - Product detail
- `POST /products/create/` - Create product (authenticated)
- `PUT /products/<id>/update/` - Update product (owner only)
- `DELETE /products/<id>/delete/` - Delete product (owner only)

### Authentication
- `POST /accounts/register/` - User registration
- `POST /accounts/login/` - User login
- `POST /accounts/logout/` - User logout
- `GET /accounts/profile/` - User profile

### Chat
- `WebSocket /ws/chat/<room_name>/` - Chat room connection

## 🎨 Customization

### Adding New Features
1. Create new Django app: `python manage.py startapp newapp`
2. Add models in `models.py`
3. Create views in `views.py`
4. Add URL patterns in `urls.py`
5. Create templates in `templates/newapp/`

### Styling
- Modify `templates/base.html` for global changes
- Add custom CSS in `static/css/`
- Override Bootstrap variables for theme customization

### Database Migration
To switch from SQLite to PostgreSQL:
1. Install psycopg2: `pip install psycopg2-binary`
2. Update `DATABASES` in `settings.py`
3. Run migrations: `python manage.py migrate`

## 🐛 Troubleshooting

### Common Issues

1. **Redis Connection Error**
   - Ensure Redis server is running
   - Check Redis configuration in `settings.py`

2. **Image Upload Issues**
   - Verify `MEDIA_ROOT` and `MEDIA_URL` settings
   - Check file permissions in media directory

3. **Migration Errors**
   - Delete migration files (keep `__init__.py`)
   - Run `makemigrations` and `migrate` again

4. **Static Files Not Loading**
   - Run `python manage.py collectstatic`
   - Check `STATIC_URL` and `STATICFILES_DIRS` settings

## 📈 Performance Optimization

For production deployment:
1. Set `DEBUG = False`
2. Use PostgreSQL or MySQL
3. Implement caching with Redis
4. Use Gunicorn with Nginx
5. Enable GZIP compression
6. Optimize images and static files

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is created for educational purposes. Feel free to use and modify as needed.

## 👨‍💻 About

This project is designed as a comprehensive learning resource for Django beginners. It covers essential concepts while building a practical, real-world application.

**Key Learning Areas:**
- Django fundamentals
- User authentication
- CRUD operations
- Real-time features
- Responsive design
- Admin interface
- Security best practices

Happy coding! 🎉
