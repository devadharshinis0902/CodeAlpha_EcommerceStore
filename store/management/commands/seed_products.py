from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.text import slugify
from store.models import Category, Product


class Command(BaseCommand):
    help = 'Seeds database with realistic sample categories, products, and test user accounts.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Starting database seeding...'))

        # 1. Create Superuser / Test Users
        if not User.objects.filter(username='admin').exists():
            admin_user = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            admin_user.first_name = 'Store'
            admin_user.last_name = 'Admin'
            admin_user.save()
            self.stdout.write(self.style.SUCCESS('Created superuser: admin / admin123'))

        if not User.objects.filter(username='testuser').exists():
            test_user = User.objects.create_user('testuser', 'testuser@example.com', 'Password123!')
            test_user.first_name = 'Alex'
            test_user.last_name = 'Morgan'
            test_user.save()
            self.stdout.write(self.style.SUCCESS('Created demo user: testuser / Password123!'))

        # 2. Sample Categories
        categories_data = [
            {
                'name': 'Audio & Headphones',
                'description': 'Premium high-fidelity wireless audio gear, noise-canceling headphones, and speakers.'
            },
            {
                'name': 'Electronics & Tech',
                'description': 'Cutting-edge gadgets, smartwatches, mechanical keyboards, and tech accessories.'
            },
            {
                'name': 'Fashion & Apparel',
                'description': 'Stylish contemporary clothing, hoodies, jackets, and modern everyday wear.'
            },
            {
                'name': 'Home & Lifestyle',
                'description': 'Minimalist home decor, smart lighting, desk accessories, and lifestyle essentials.'
            },
            {
                'name': 'Footwear & Sneakers',
                'description': 'Performance running shoes, casual sneakers, and ergonomic footwear.'
            }
        ]

        category_objs = {}
        for cat in categories_data:
            obj, created = Category.objects.get_or_create(
                name=cat['name'],
                defaults={
                    'slug': slugify(cat['name']),
                    'description': cat['description']
                }
            )
            category_objs[cat['name']] = obj

        # 3. Sample Products
        products_data = [
            {
                'category': category_objs['Audio & Headphones'],
                'name': 'AeroSound Pro Wireless ANC Headphones',
                'price': 199.99,
                'stock': 25,
                'rating': 4.8,
                'image_url': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=800&q=80',
                'description': 'Experience studio-quality audio with industry-leading Active Noise Cancellation (ANC). Features 40-hour battery life, ultra-soft memory foam earcups, and dual multi-point Bluetooth connection.'
            },
            {
                'category': category_objs['Audio & Headphones'],
                'name': 'Pulse Mini Portable Bluetooth Speaker',
                'price': 49.50,
                'stock': 40,
                'rating': 4.5,
                'image_url': 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?auto=format&fit=crop&w=800&q=80',
                'description': 'Compact IPX7 waterproof Bluetooth speaker delivering punchy 360-degree sound. Ideal for outdoor adventures, poolside parties, or home desk listening.'
            },
            {
                'category': category_objs['Electronics & Tech'],
                'name': 'ChronoFit Pro Smartwatch',
                'price': 149.00,
                'stock': 18,
                'rating': 4.7,
                'image_url': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=800&q=80',
                'description': 'Sleek AMOLED smartwatch with continuous heart rate monitoring, GPS tracking, sleep analytics, and over 50 workout modes. Water resistant up to 50 meters.'
            },
            {
                'category': category_objs['Electronics & Tech'],
                'name': 'KeyCraft RGB Mechanical Keyboard',
                'price': 119.99,
                'stock': 12,
                'rating': 4.9,
                'image_url': 'https://images.unsplash.com/photo-1587829741301-dc798b83add3?auto=format&fit=crop&w=800&q=80',
                'description': 'Customizable 75% hot-swappable mechanical keyboard equipped with linear tactile switches, per-key RGB backlight, and durable PBT keycaps.'
            },
            {
                'category': category_objs['Electronics & Tech'],
                'name': 'Ergonomic Precision Wireless Mouse',
                'price': 39.99,
                'stock': 30,
                'rating': 4.6,
                'image_url': 'https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?auto=format&fit=crop&w=800&q=80',
                'description': 'Sculpted ergonomic design reduces wrist strain during extended work hours. Multi-device switching with hyper-fast scrolling wheel.'
            },
            {
                'category': category_objs['Fashion & Apparel'],
                'name': 'Urban Minimalist Fleece Hoodie',
                'price': 65.00,
                'stock': 35,
                'rating': 4.4,
                'image_url': 'https://images.unsplash.com/photo-1556905055-8f358a7a47b2?auto=format&fit=crop&w=800&q=80',
                'description': 'Premium organic heavy cotton hoodie featuring a tailored relaxed fit, double-lined hood, and kangaroo front pocket. Exceptionally warm and soft.'
            },
            {
                'category': category_objs['Fashion & Apparel'],
                'name': 'Classic Denim Trucker Jacket',
                'price': 89.95,
                'stock': 15,
                'rating': 4.6,
                'image_url': 'https://images.unsplash.com/photo-1576995853123-5a10305d93c0?auto=format&fit=crop&w=800&q=80',
                'description': 'Timeless vintage wash denim jacket made from 100% durable cotton denim. Button front closure with dual chest flap pockets.'
            },
            {
                'category': category_objs['Home & Lifestyle'],
                'name': 'Minimalist Ceramic Desk Lamp',
                'price': 55.00,
                'stock': 20,
                'rating': 4.8,
                'image_url': 'https://images.unsplash.com/photo-1507473885765-e6ed057f782c?auto=format&fit=crop&w=800&q=80',
                'description': 'Scandinavian inspired dimmable LED ceramic desk lamp with warm tone illumination. Adds clean aesthetic charm to any study or bedroom workspace.'
            },
            {
                'category': category_objs['Home & Lifestyle'],
                'name': 'Insulated Stainless Steel Water Bottle',
                'price': 28.50,
                'stock': 50,
                'rating': 4.9,
                'image_url': 'https://images.unsplash.com/photo-1602143407151-7111542de6e8?auto=format&fit=crop&w=800&q=80',
                'description': 'Double-wall vacuum insulated flask keeps beverages icy cold for 24 hours or piping hot for 12 hours. BPA-free leak-proof lid.'
            },
            {
                'category': category_objs['Footwear & Sneakers'],
                'name': 'CloudStride Nitro Running Shoes',
                'price': 129.99,
                'stock': 8,
                'rating': 4.7,
                'image_url': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=800&q=80',
                'description': 'High-performance neutral running shoes with responsive nitrogen-infused foam cushioning and breathable engineered mesh upper.'
            },
            {
                'category': category_objs['Footwear & Sneakers'],
                'name': 'Classic Canvas Retro Sneakers',
                'price': 59.95,
                'stock': 22,
                'rating': 4.3,
                'image_url': 'https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?auto=format&fit=crop&w=800&q=80',
                'description': 'Versatile low-top canvas sneakers featuring vulcanized rubber soles and padded insoles for all-day comfort.'
            }
        ]

        for p_data in products_data:
            slug = slugify(p_data['name'])
            Product.objects.update_or_create(
                slug=slug,
                defaults={
                    'category': p_data['category'],
                    'name': p_data['name'],
                    'price': p_data['price'],
                    'stock': p_data['stock'],
                    'rating': p_data['rating'],
                    'image_url': p_data['image_url'],
                    'description': p_data['description']
                }
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {len(products_data)} products across {len(categories_data)} categories!'))
