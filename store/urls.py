from django.urls import path
from . import views

urlpatterns = [
    # Products & Catalog
    path('', views.product_list_view, name='product_list'),
    path('product/<slug:slug>/', views.product_detail_view, name='product_detail'),
    
    # Shopping Cart
    path('cart/', views.cart_view, name='cart'),
    path('api/cart-sync/', views.api_cart_sync, name='api_cart_sync'),

    # Authentication
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Checkout & Orders
    path('checkout/', views.checkout_view, name='checkout'),
    path('order-confirmation/<int:order_id>/', views.order_confirmation_view, name='order_confirmation'),
    path('orders/', views.order_history_view, name='order_history'),
    path('order/<int:order_id>/', views.order_detail_view, name='order_detail'),
]
