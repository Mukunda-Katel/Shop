from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list, name='list'),
    path('<int:pk>/', views.product_detail, name='detail'),
    path('create/', views.create_product, name='create'),
    path('<int:pk>/update/', views.update_product, name='update'),
    path('<int:pk>/delete/', views.delete_product, name='delete'),
    path('<int:pk>/like/', views.toggle_like, name='toggle_like'),
    path('my-products/', views.my_products, name='my_products'),
]
