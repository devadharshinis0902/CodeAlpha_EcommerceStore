import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from .models import Category, Product, Order, OrderItem
from .forms import UserRegistrationForm, UserLoginForm, CheckoutForm


def product_list_view(request):
    """Home / Product Listing Page with Search & Category Filtering"""
    products = Product.objects.all()
    categories = Category.objects.all()
    
    # Category Filter
    selected_category_slug = request.GET.get('category', '').strip()
    selected_category = None
    if selected_category_slug:
        selected_category = get_object_or_404(Category, slug=selected_category_slug)
        products = products.filter(category=selected_category)
        
    # Search Filter
    search_query = request.GET.get('q', '').strip()
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query) |
            Q(category__name__icontains=search_query)
        )

    # Sorting
    sort_option = request.GET.get('sort', '').strip()
    if sort_option == 'price_asc':
        products = products.order_by('price')
    elif sort_option == 'price_desc':
        products = products.order_by('-price')
    elif sort_option == 'rating':
        products = products.order_by('-rating')
    else:
        products = products.order_by('-created_at')

    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
        'search_query': search_query,
        'sort_option': sort_option,
        'total_products': products.count(),
    }
    return render(request, 'store/product_list.html', context)


def product_detail_view(request, slug):
    """Single Product Details Page"""
    product = get_object_or_404(Product, slug=slug)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    
    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'store/product_detail.html', context)


def cart_view(request):
    """Shopping Cart Page"""
    return render(request, 'store/cart.html')


def register_view(request):
    """User Registration Page"""
    if request.user.is_authenticated:
        return redirect('product_list')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            user.save()

            # Automatically log in the user
            login(request, user)
            messages.success(request, f"Welcome to Simple E-commerce Store, {user.first_name or user.username}! Your account has been created.")
            return redirect('product_list')
        else:
            messages.error(request, "Please correct the errors below to complete your registration.")
    else:
        form = UserRegistrationForm()

    return render(request, 'store/register.html', {'form': form})


def login_view(request):
    """User Login Page"""
    if request.user.is_authenticated:
        return redirect('product_list')

    next_url = request.GET.get('next', 'product_list')

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data.get('username').strip()
            password = form.cleaned_data.get('password')

            # Check if user entered email instead of username
            username = username_or_email
            if '@' in username_or_email:
                try:
                    user_obj = User.objects.get(email__iexact=username_or_email)
                    username = user_obj.username
                except User.DoesNotExist:
                    username = username_or_email

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.first_name or user.username}!")
                return redirect(next_url)
            else:
                messages.error(request, "Invalid username/email or password. Please try again.")
    else:
        form = UserLoginForm()

    return render(request, 'store/login.html', {'form': form, 'next': next_url})


def logout_view(request):
    """User Logout"""
    logout(request)
    messages.info(request, "You have been logged out successfully.")
    return redirect('product_list')


@login_required(login_url='login')
def checkout_view(request):
    """Order Checkout Page & Order Processing"""
    user = request.user
    
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        cart_data_raw = request.POST.get('cart_data', '[]')
        
        try:
            cart_items = json.loads(cart_data_raw)
        except json.JSONDecodeError:
            cart_items = []

        if not cart_items:
            messages.error(request, "Your cart is empty. Please add products before checking out.")
            return redirect('cart')

        if form.is_valid():
            # Validate cart stock & calculate total on backend
            total_amount = 0
            order_items_to_create = []
            
            for item in cart_items:
                product_id = item.get('id')
                quantity = int(item.get('quantity', 1))
                
                try:
                    product = Product.objects.get(id=product_id)
                except Product.DoesNotExist:
                    messages.error(request, f"One of the products in your cart is no longer available.")
                    return redirect('cart')

                if quantity > product.stock:
                    messages.error(request, f"Sorry, only {product.stock} units of '{product.name}' are available.")
                    return redirect('cart')

                subtotal = product.price * quantity
                total_amount += subtotal
                order_items_to_create.append({
                    'product': product,
                    'product_name': product.name,
                    'price': product.price,
                    'quantity': quantity
                })

            # Save Order
            order = form.save(commit=False)
            order.user = user
            order.total_amount = total_amount
            order.status = 'Processing'
            order.save()

            # Save OrderItems & adjust product stock
            for item_data in order_items_to_create:
                OrderItem.objects.create(
                    order=order,
                    product=item_data['product'],
                    product_name=item_data['product_name'],
                    price=item_data['price'],
                    quantity=item_data['quantity']
                )
                # Deduct stock
                product = item_data['product']
                product.stock -= item_data['quantity']
                product.save()

            messages.success(request, f"Order #{order.id} placed successfully!")
            return redirect('order_confirmation', order_id=order.id)
        else:
            messages.error(request, "Please fill out all required checkout fields correctly.")
    else:
        # Pre-fill user information
        initial_data = {
            'full_name': f"{user.first_name} {user.last_name}".strip() or user.username,
            'email': user.email,
        }
        form = CheckoutForm(initial=initial_data)

    return render(request, 'store/checkout.html', {'form': form})


@login_required(login_url='login')
def order_confirmation_view(request, order_id):
    """Order Confirmation Receipt Page"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'store/order_confirmation.html', {'order': order})


@login_required(login_url='login')
def order_history_view(request):
    """Logged-in User Order History Page"""
    orders = Order.objects.filter(user=request.user).prefetch_related('items')
    return render(request, 'store/orders.html', {'orders': orders})


@login_required(login_url='login')
def order_detail_view(request, order_id):
    """Detailed View for a Specific Past Order"""
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'store/order_detail.html', {'order': order})


def api_cart_sync(request):
    """API endpoint to validate cart items, current prices, stock, and return refreshed items"""
    if request.method != 'POST':
        return JsonResponse({'error': 'POST required'}, status=400)

    try:
        data = json.loads(request.body)
        raw_cart = data.get('cart', [])
    except Exception:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    validated_items = []
    total_amount = 0
    warnings = []

    for item in raw_cart:
        p_id = item.get('id')
        qty = int(item.get('quantity', 1))
        
        try:
            prod = Product.objects.get(id=p_id)
            if qty > prod.stock:
                qty = max(1, prod.stock)
                warnings.append(f"Adjusted '{prod.name}' quantity to available stock ({prod.stock}).")
            
            subtotal = float(prod.price) * qty
            total_amount += subtotal

            validated_items.append({
                'id': prod.id,
                'name': prod.name,
                'slug': prod.slug,
                'price': float(prod.price),
                'image': prod.get_image_src(),
                'stock': prod.stock,
                'quantity': qty,
                'subtotal': subtotal
            })
        except Product.DoesNotExist:
            warnings.append("One or more items in your cart were removed as they are no longer available.")

    return JsonResponse({
        'items': validated_items,
        'total': total_amount,
        'warnings': warnings
    })
