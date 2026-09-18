# Simple E-commerce Store (CodeAlpha Internship - Task 1)

A complete, beginner-to-intermediate full-stack e-commerce web application built for **CodeAlpha Full Stack Development Internship (Task 1)** using **Python Django**, **SQLite**, **HTML5**, **CSS3**, and **Vanilla JavaScript**.

---

## 🌟 Project Overview
The **Simple E-commerce Store** is a feature-complete online shopping application featuring a dynamic product catalog, category filtering, search functionality, interactive cart management with `localStorage` persistence, Django user authentication, checkout processing, order database recording, and user order history tracking.

---

## 🚀 Key Features

### 1. Product Catalog & Search
- Interactive home page displaying products with images, prices, categories, ratings, and stock indicators.
- Live product search by name, category, or keywords.
- Category filtering (Audio, Electronics, Fashion, Home, Footwear).
- Product sorting by price (low/high), rating, and recency.

### 2. Detailed Product View
- Dedicated detail page for every product with high-resolution image preview.
- Complete specifications and description.
- Quantity selector with stock availability safeguards.
- Instant "Add to Cart" interaction.

### 3. Persistent Shopping Cart
- Built with Vanilla JavaScript and `localStorage`.
- Real-time cart badge counter in navigation bar.
- Adjust product quantities or remove items directly.
- Prevents selecting quantities exceeding available stock.
- Calculates subtotal and grand total dynamically.
- Cart state persists across page refreshes and tab navigation.

### 4. User Authentication & Authorization
- Built-in Django User Authentication (`django.contrib.auth`).
- Registration with form validation (password matching, unique email/username checks).
- Login with Username or Email support.
- Protected access control: unauthorized users are redirected to login when attempting to access checkout or order history.

### 5. Checkout & Order Processing
- Customer shipping address form with validation.
- Simulated payment options (Cash on Delivery, Demo Credit Card, Demo UPI).
- Database recording of `Order` and itemized `OrderItem` records upon submission.
- Automatic stock deduction from inventory.

### 6. Order Confirmation & Order History
- Instant printable order receipt page with unique Order ID and summary.
- Dedicated "My Orders" history page for logged-in users.
- Individual order detail breakdown view.

---

## 🛠️ Technology Stack
- **Backend Framework**: Python Django 4.2+
- **Database**: SQLite3
- **Frontend Logic**: Vanilla JavaScript (ES6) - *No React, Angular, or external JS frameworks*
- **Styling**: Modern CSS3 (CSS Variables, Flexbox, Grid, Responsive Design)
- **Markup**: HTML5 Templates with Django Template Language (DTL)

---

## 📂 Project Structure

```
CodeAlpha_EcommerceStore/
│
├── manage.py                   # Django management script
├── requirements.txt            # Project dependencies
├── README.md                   # Documentation
├── .gitignore                  # Git ignore configuration
├── db.sqlite3                  # SQLite Database (generated)
│
├── store_project/              # Core Django Project Configuration
│   ├── __init__.py
│   ├── settings.py             # App settings, DB, static/media paths
│   ├── urls.py                 # Root URL router
│   ├── asgi.py
│   └── wsgi.py
│
├── store/                      # Store Application
│   ├── migrations/             # Database migration files
│   ├── management/
│   │   └── commands/
│   │       └── seed_products.py# Data seeder for categories & products
│   ├── __init__.py
│   ├── admin.py                # Django Admin configuration
│   ├── apps.py
│   ├── forms.py                # Registration, Login & Checkout forms
│   ├── models.py               # Category, Product, Order, OrderItem models
│   ├── urls.py                 # Application routes
│   └── views.py                # Business logic views
│
├── templates/                  # HTML Templates
│   ├── base.html               # Main layout template with Navbar & Footer
│   └── store/
│       ├── product_list.html   # Home product catalog
│       ├── product_detail.html # Single product details view
│       ├── cart.html           # Shopping cart page
│       ├── register.html       # User registration page
│       ├── login.html          # User login page
│       ├── checkout.html       # Order checkout page
│       ├── order_confirmation.html # Receipt confirmation
│       ├── orders.html         # User order history
│       └── order_detail.html   # Detailed order view
│
└── static/                     # Static Assets
    ├── css/
    │   └── style.css           # Global custom stylesheet
    └── js/
        ├── main.js             # Navigation & toast alerts
        └── cart.js             # Cart engine & localStorage persistence
```

---

## ⚡ Quick Setup & Installation Guide

### Step 1: Open Terminal / PowerShell
Open your terminal in the project directory:
```bash
cd C:\Users\dellp\Documents\CodeAlpha_EcommerceStore
```

### Step 2: Create & Activate Virtual Environment
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Seed Sample Products & Test Accounts
Run the automated seed command to populate realistic categories, products, images, and demo accounts:
```bash
python manage.py seed_products
```

### Step 6: Start Development Server
```bash
python manage.py runserver
```
Open your browser and navigate to: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 🔑 Demo Test Accounts

| Role | Username | Password | Email |
| :--- | :--- | :--- | :--- |
| **Superuser / Admin** | `admin` | `admin123` | `admin@example.com` |
| **Demo Customer** | `testuser` | `Password123!` | `testuser@example.com` |

---

## 📋 Manual Testing Checklist

- [x] **Product Listing**: Home page displays seeded products with images, prices, stock badges.
- [x] **Category Filter**: Filtering by 'Audio', 'Electronics', 'Fashion' displays corresponding products.
- [x] **Product Search**: Searching "Headphones" returns matching products.
- [x] **Product Details**: Clicking a product opens the detail page with quantity picker and stock limit alerts.
- [x] **Cart Management**: Add to cart, adjust quantities (+/-), remove item, check cart badge update.
- [x] **Cart Persistence**: Refreshing the browser preserves all cart items.
- [x] **User Auth**: Registration creates a user account; Login authenticates user and updates navbar.
- [x] **Protected Pages**: Accessing `/checkout/` or `/orders/` while logged out redirects to `/login/`.
- [x] **Order Checkout**: Completing checkout creates `Order` & `OrderItem` records in SQLite, deducts stock, and redirects to Order Confirmation.
- [x] **Cart Cleanup**: Placing an order empties the cart.
- [x] **Order History**: Logged-in user can inspect placed orders under `/orders/`.

---

## 🐙 Uploading to GitHub

1. Initialize git repository (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit: CodeAlpha Simple E-commerce Store"
   ```
2. Create repository `CodeAlpha_EcommerceStore` on GitHub.
3. Link and push:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/CodeAlpha_EcommerceStore.git
   git branch -M main
   git push -u origin main
   ```

---

## 🎬 Video Presentation Demonstration Guide
When recording your CodeAlpha internship submission video, demonstrate the following steps:
1. Show project structure in VS Code.
2. Run `python manage.py check` and `python manage.py runserver`.
3. Open browser at `http://127.0.0.1:8000`.
4. Demonstrate product browsing, search, category filter, and product detail view.
5. Add items to cart, refresh page to show persistence.
6. Register a new user or log in as `testuser`.
7. Proceed to checkout, fill shipping details, and place an order.
8. Show Order Confirmation page.
9. Open "My Orders" to show recorded order in SQLite.
10. Log in to Django Admin (`/admin`) to show `Order` and `Product` models.
