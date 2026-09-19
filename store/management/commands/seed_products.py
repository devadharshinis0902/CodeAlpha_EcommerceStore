from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.text import slugify
from store.models import Category, Product


class Command(BaseCommand):
    help = 'Seeds database with realistic sample fashion categories, products, and test user accounts.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Starting Fashion Store database seeding...'))

        # 1. Create Superuser / Test Users
        if not User.objects.filter(username='admin').exists():
            admin_user = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            admin_user.first_name = 'Fashion'
            admin_user.last_name = 'Admin'
            admin_user.save()
            self.stdout.write(self.style.SUCCESS('Created superuser: admin / admin123'))

        if not User.objects.filter(username='testuser').exists():
            test_user = User.objects.create_user('testuser', 'testuser@example.com', 'Password123!')
            test_user.first_name = 'Sophia'
            test_user.last_name = 'Styles'
            test_user.save()
            self.stdout.write(self.style.SUCCESS('Created demo user: testuser / Password123!'))

        # 2. Fashion Categories
        categories_data = [
            {'name': "Women's Fashion", 'description': "Trendy clothing, ethnic wear, and modern fashion for women."},
            {'name': "Men's Fashion", 'description': "Smart casuals, formal shirts, jackets, and denim for men."},
            {'name': "Kids", 'description': "Adorable and comfortable clothing for children of all ages."},
            {'name': "Dresses", 'description': "Elegant evening gowns, casual maxi dresses, and party wear."},
            {'name': "Tops", 'description': "Stylish blouses, t-shirts, crop tops, and tunic tops."},
            {'name': "Jeans", 'description': "Slim-fit, high-rise, and relaxed denim jeans."},
            {'name': "Sarees", 'description': "Handcrafted silk, chiffon, and designer sarees for occasions."},
            {'name': "Kurtis", 'description': "Traditional and contemporary ethnic kurtis and tunic dresses."},
            {'name': "Footwear", 'description': "Trendy sneakers, leather loafers, elegant heels, and sandals."},
            {'name': "Handbags", 'description': "Chic shoulder bags, luxury totes, clutches, and crossbody bags."},
            {'name': "Jewellery", 'description': "Gold-plated necklaces, crystal earrings, and fine fashion jewellery."},
            {'name': "Accessories", 'description': "Polarized sunglasses, luxury wristwatches, and genuine leather wallets."}
        ]

        category_objs = {}
        for cat in categories_data:
            obj, created = Category.objects.get_or_create(
                slug=slugify(cat['name']),
                defaults={
                    'name': cat['name'],
                    'description': cat['description']
                }
            )
            category_objs[cat['name']] = obj

        # 3. Fashion Products Data
        products_data = [
            # Women's & Dresses & Kurtis
            {
                'category': category_objs['Dresses'],
                'name': 'Floral Breeze Summer Maxi Dress',
                'price': 49.99,
                'original_price': 89.99,
                'stock': 25,
                'rating': 4.8,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?auto=format&fit=crop&w=800&q=80',
                'description': 'A breathable, elegant floral maxi dress crafted from premium lightweight chiffon. Perfect for summer brunches, beach outings, and garden parties.'
            },
            {
                'category': category_objs['Kurtis'],
                'name': 'Hand-Block Printed Cotton Kurti',
                'price': 29.99,
                'original_price': 49.99,
                'stock': 30,
                'rating': 4.7,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1583391733956-6c78276477e2?auto=format&fit=crop&w=800&q=80',
                'description': 'Traditional hand-block printed pure cotton kurti featuring delicate embroidery on the neckline and a comfortable straight fit.'
            },
            {
                'category': category_objs['Sarees'],
                'name': 'Royal Banarasi Silk Designer Saree',
                'price': 79.99,
                'original_price': 149.99,
                'stock': 15,
                'rating': 4.9,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1610030469983-98e550d6193c?auto=format&fit=crop&w=800&q=80',
                'description': 'Luxurious Banarasi silk saree adorned with intricate gold zari weave. Comes with an unstitched matching blouse piece.'
            },
            {
                'category': category_objs['Jeans'],
                'name': 'High-Waisted Slim Fit Denim Jeans',
                'price': 39.99,
                'original_price': 69.99,
                'stock': 20,
                'rating': 4.6,
                'is_featured': False,
                'image_url': 'https://images.unsplash.com/photo-1541099649105-f69ad21f3246?auto=format&fit=crop&w=800&q=80',
                'description': 'Flattering high-rise denim jeans with optimal stretch and durable double-stitched seams. Essential wardrobe staple.'
            },

            # Men's Fashion
            {
                'category': category_objs["Men's Fashion"],
                'name': 'Men\'s Casual Linen Button-Down Shirt',
                'price': 34.99,
                'original_price': 59.99,
                'stock': 35,
                'rating': 4.6,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1596755094514-f87e34085b2c?auto=format&fit=crop&w=800&q=80',
                'description': 'Airy 100% organic linen casual shirt featuring a spread collar and chest pocket. Tailored for effortless summer style.'
            },
            {
                'category': category_objs["Men's Fashion"],
                'name': 'Men\'s Slim Fit Stretch Denim Jeans',
                'price': 44.99,
                'original_price': 79.99,
                'stock': 22,
                'rating': 4.7,
                'is_featured': False,
                'image_url': 'https://images.unsplash.com/photo-1542272604-780c96856552?auto=format&fit=crop&w=800&q=80',
                'description': 'Modern slim-fit jeans constructed from premium indigo denim with comfort-stretch technology for all-day mobility.'
            },
            {
                'category': category_objs["Men's Fashion"],
                'name': 'Classic Oxford Cotton Formal Shirt',
                'price': 39.99,
                'original_price': 69.99,
                'stock': 18,
                'rating': 4.8,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?auto=format&fit=crop&w=800&q=80',
                'description': 'Crisp Oxford cotton formal shirt designed with a button-down collar and wrinkle-resistant fabric. Ideal for business and formal wear.'
            },
            {
                'category': category_objs['Tops'],
                'name': 'Essential Organic Cotton Crewneck T-Shirt',
                'price': 19.99,
                'original_price': 34.99,
                'stock': 50,
                'rating': 4.5,
                'is_featured': False,
                'image_url': 'https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=800&q=80',
                'description': 'Ultra-soft combed organic cotton t-shirt with a pre-shrunk fit and durable ribbed crew collar.'
            },

            # Handbags & Accessories
            {
                'category': category_objs['Handbags'],
                'name': 'Elegance Genuine Leather Shoulder Handbag',
                'price': 54.99,
                'original_price': 99.99,
                'stock': 12,
                'rating': 4.9,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1584917865442-de89df76afd3?auto=format&fit=crop&w=800&q=80',
                'description': 'Spacious handcrafted leather tote handbag with multi-zip compartments and detachable shoulder strap.'
            },
            {
                'category': category_objs['Accessories'],
                'name': 'Polarized UV400 Classic Aviator Sunglasses',
                'price': 29.99,
                'original_price': 59.99,
                'stock': 40,
                'rating': 4.7,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1572635196237-14b3f281503f?auto=format&fit=crop&w=800&q=80',
                'description': 'Lightweight metal frame aviator sunglasses featuring HD glare-blocking polarized lenses with full UV400 protection.'
            },
            {
                'category': category_objs['Accessories'],
                'name': 'Minimalist Steel Chronograph Wrist Watch',
                'price': 79.99,
                'original_price': 149.99,
                'stock': 15,
                'rating': 4.8,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1524805444758-089113d48a6d?auto=format&fit=crop&w=800&q=80',
                'description': 'Sleek stainless steel wrist watch with Japanese quartz movement, scratch-resistant sapphire glass, and 30m water resistance.'
            },

            # Footwear
            {
                'category': category_objs['Footwear'],
                'name': 'Minimalist Urban White Sneakers',
                'price': 49.99,
                'original_price': 89.99,
                'stock': 28,
                'rating': 4.7,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1549298916-b41d501d3772?auto=format&fit=crop&w=800&q=80',
                'description': 'Versatile low-top leather sneakers with cushioned insoles and durable anti-slip rubber outsole.'
            },
            {
                'category': category_objs['Footwear'],
                'name': 'Women\'s Elegant Strap Heel Sandals',
                'price': 59.99,
                'original_price': 109.99,
                'stock': 14,
                'rating': 4.6,
                'is_featured': False,
                'image_url': 'https://images.unsplash.com/photo-1543163521-1bf539c55dd2?auto=format&fit=crop&w=800&q=80',
                'description': 'Chic ankle strap high heels designed for evening wear and special celebrations.'
            },

            # Jewellery
            {
                'category': category_objs['Jewellery'],
                'name': 'Gold Plated Minimalist Pendant Necklace',
                'price': 24.99,
                'original_price': 49.99,
                'stock': 30,
                'rating': 4.8,
                'is_featured': False,
                'image_url': 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?auto=format&fit=crop&w=800&q=80',
                'description': '18k gold plated dainty pendant necklace crafted from hypoallergenic brass.'
            },
            {
                'category': category_objs['Jewellery'],
                'name': 'Crystal Chandelier Drop Earrings',
                'price': 18.99,
                'original_price': 34.99,
                'stock': 25,
                'rating': 4.5,
                'is_featured': False,
                'image_url': 'https://images.unsplash.com/photo-1630019852942-f89202989a59?auto=format&fit=crop&w=800&q=80',
                'description': 'Sparkling cubic zirconia crystal earrings for weddings and evening galas.'
            },

            # Kids
            {
                'category': category_objs['Kids'],
                'name': 'Kids Printed Cotton Outfit Set',
                'price': 22.99,
                'original_price': 39.99,
                'stock': 35,
                'rating': 4.6,
                'is_featured': False,
                'image_url': 'https://images.unsplash.com/photo-1519238263530-99bdd11df2ea?auto=format&fit=crop&w=800&q=80',
                'description': 'Soft and breathable 100% cotton printed shirt and shorts combo set for kids.'
            }
        ]

        # Clean existing non-fashion products if re-seeding
        Product.objects.all().delete()

        for p_data in products_data:
            slug = slugify(p_data['name'])
            Product.objects.create(
                category=p_data['category'],
                name=p_data['name'],
                slug=slug,
                price=p_data['price'],
                original_price=p_data['original_price'],
                stock=p_data['stock'],
                rating=p_data['rating'],
                is_featured=p_data['is_featured'],
                image_url=p_data['image_url'],
                description=p_data['description']
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {len(products_data)} fashion products across {len(categories_data)} categories!'))
