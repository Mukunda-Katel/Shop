@echo off
echo Starting ShoppingMart Django Server...
echo.
echo Admin credentials:
echo Username: admin
echo Password: admin123
echo.
echo Demo seller credentials:
echo Username: demo_seller
echo Password: demopass123
echo.
echo Server will start at http://127.0.0.1:8000
echo Press Ctrl+C to stop the server
echo.
python manage.py runserver
