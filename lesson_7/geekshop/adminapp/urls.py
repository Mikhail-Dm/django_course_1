from django.urls import path
from adminapp import views as admin_views

appname = 'adminapp'

urlpatterns = [
    path('users/create/', admin_views.user_create, 'user_create'),
    path('users/', admin_views.users, 'users'),
    path('users/update/<int:pk>/', admin_views.user_update, 'user_update'),
    path('users/delete/<int:pk>/', admin_views.user_delete, 'user_delete'),

    path('categories/create/', admin_views.category_create, 'category_create'),
    path('categories/', admin_views.categories, 'categories'),
    path('categories/update/<int:pk>/', admin_views.category_update, 'category_update'),
    path('categories/delete/<int:pk>/', admin_views.category_delete, 'category_delete'),

    path('products/create/', admin_views.product_create, 'product_create'),
    path('products/<int:pk>/', admin_views.products, 'products'),
    path('products/update/<int:pk>/', admin_views.product_update, 'product_update'),
    path('products/delete/<int:pk>/', admin_views.product_delete, 'product_delete'),
    path('products/details/<int:pk>/', admin_views.product_detail, 'product_detail'),
]