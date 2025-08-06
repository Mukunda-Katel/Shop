import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopping_mart.settings')
django.setup()

from django.contrib.auth.models import User

try:
    admin = User.objects.get(username='admin')
    admin.set_password('admin123')
    admin.save()
    print("Password 'admin123' set for admin user successfully!")
except User.DoesNotExist:
    print("Admin user not found.")
