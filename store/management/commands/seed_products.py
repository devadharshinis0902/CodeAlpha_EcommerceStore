from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils.text import slugify
from store.models import Category, Product


class Command(BaseCommand):
    help = 'Seeds database with comprehensive fashion categories and 40+ products with Indian Rupee (₹) pricing.'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Starting Rupee Fashion Store database seeding...'))

        # 1. Create Superuser / Test Users
        if not User.objects.filter(username='admin').exists():
            admin_user = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            admin_user.first_name = 'Fashion'
            admin_user.last_name = 'Admin'
            admin_user.save()
            self.stdout.write(self.style.SUCCESS('Created superuser: admin / admin123'))

        if not User.objects.filter(username='testuser').exists():
            test_user = User.objects.create_user('testuser', 'testuser@example.com', 'Password123!')
            test_user.first_name = 'Priya'
            test_user.last_name = 'Sharma'
            test_user.save()
            self.stdout.write(self.style.SUCCESS('Created demo user: testuser / Password123!'))

        # 2. Fashion Categories
        categories_data = [
            {'name': "Women's Fashion", 'description': "Trendy clothing, ethnic wear, and modern fashion for women."},
            {'name': "Men's Fashion", 'description': "Smart casuals, formal shirts, jackets, and denim for men."},
            {'name': "Kids", 'description': "Adorable and comfortable clothing for children of all ages."},
            {'name': "Dresses", 'description': "Elegant evening gowns, casual maxi dresses, and party wear."},
            {'name': "Tops", 'description': "Stylish blouses, t-shirts, crop tops, and tunic tops."},
            {'name': "Jeans", 'description': "Slim-fit, high-rise, and relaxed denim jeans for men and women."},
            {'name': "Sarees", 'description': "Handcrafted silk, chiffon, georgette, and designer sarees."},
            {'name': "Kurtis", 'description': "Traditional Chikankari, hand-block printed, and modern kurtis."},
            {'name': "Footwear", 'description': "Trendy sneakers, leather loafers, elegant heels, and ethnic juttis."},
            {'name': "Handbags", 'description': "Chic shoulder bags, luxury totes, clutches, and crossbody bags."},
            {'name': "Jewellery", 'description': "Gold-plated necklaces, Kundan sets, crystal earrings, and silver rings."},
            {'name': "Accessories", 'description': "Polarized sunglasses, luxury wristwatches, leather belts, and wallets."}
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

        # 3. 40+ Fashion Products (INR Pricing)
        products_data = [
            # DRESSES
            {
                'category': category_objs['Dresses'],
                'name': 'Floral Breeze Summer Maxi Dress',
                'price': 1799.00,
                'original_price': 3199.00,
                'stock': 25,
                'rating': 4.8,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?auto=format&fit=crop&w=800&q=80',
                'description': 'A breathable, elegant floral maxi dress crafted from premium lightweight chiffon. Perfect for summer brunches, beach outings, and garden parties.'
            },
            {
                'category': category_objs['Dresses'],
                'name': 'Satin Slip Evening Party Midi Dress',
                'price': 2199.00,
                'original_price': 3999.00,
                'stock': 18,
                'rating': 4.7,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1595777457583-95e059d581b8?auto=format&fit=crop&w=800&q=80',
                'description': 'Luxurious cowl-neck satin midi dress designed for evening parties and cocktail dinners.'
            },
            {
                'category': category_objs['Dresses'],
                'name': 'A-Line Polka Print Wrap Dress',
                'price': 1499.00,
                'original_price': 2699.00,
                'stock': 30,
                'rating': 4.6,
                'is_featured': False,
                'image_url': 'https://images.unsplash.com/photo-1515886657613-9f3515b0c78f?auto=format&fit=crop&w=800&q=80',
                'description': 'Classic retro polka print wrap dress with adjustable waist tie and flare hemline.'
            },

            # KURTIS
            {
                'category': category_objs['Kurtis'],
                'name': 'Hand-Block Printed Cotton Kurti',
                'price': 1199.00,
                'original_price': 1999.00,
                'stock': 30,
                'rating': 4.7,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1583391733956-6c78276477e2?auto=format&fit=crop&w=800&q=80',
                'description': 'Traditional hand-block printed pure cotton kurti featuring delicate embroidery on the neckline and a comfortable straight fit.'
            },
            {
                'category': category_objs['Kurtis'],
                'name': 'Chikankari Hand-Embroidered Georgette Kurti',
                'price': 1699.00,
                'original_price': 2999.00,
                'stock': 22,
                'rating': 4.9,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1617627143750-d86bc21e42bb?auto=format&fit=crop&w=800&q=80',
                'description': 'Exquisite Lucknowi Chikankari hand-embroidered georgette kurti set with matching inner slip.'
            },
            {
                'category': category_objs['Kurtis'],
                'name': 'Festive Rayon Anarkali Tunic Kurti',
                'price': 1999.00,
                'original_price': 3499.00,
                'stock': 20,
                'rating': 4.6,
                'is_featured': False,
                'image_url': 'https://images.unsplash.com/photo-1610030469983-98e550d6193c?auto=format&fit=crop&w=800&q=80',
                'description': 'Flowy printed rayon Anarkali kurti embellished with gota patti work for festive celebrations.'
            },

            # SAREES
            {
                'category': category_objs['Sarees'],
                'name': 'Royal Banarasi Silk Designer Saree',
                'price': 3999.00,
                'original_price': 7499.00,
                'stock': 15,
                'rating': 4.9,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1610030469983-98e550d6193c?auto=format&fit=crop&w=800&q=80',
                'description': 'Luxurious Banarasi silk saree adorned with intricate gold zari weave. Comes with an unstitched matching blouse piece.'
            },
            {
                'category': category_objs['Sarees'],
                'name': 'Kanjeevaram Soft Silk Traditional Saree',
                'price': 4599.00,
                'original_price': 8999.00,
                'stock': 12,
                'rating': 4.8,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1617627143750-d86bc21e42bb?auto=format&fit=crop&w=800&q=80',
                'description': 'Rich South Indian Kanjeevaram soft silk saree featuring temple border zari design.'
            },
            {
                'category': category_objs['Sarees'],
                'name': 'Organza Floral Print Designer Saree',
                'price': 1499.00,
                'original_price': 2799.00,
                'stock': 25,
                'rating': 4.5,
                'is_featured': False,
                'image_url': 'https://images.unsplash.com/photo-1583391733956-6c78276477e2?auto=format&fit=crop&w=800&q=80',
                'description': 'Lightweight pastel organza saree featuring romantic digital floral prints.'
            },

            # WOMEN'S FASHION
            {
                'category': category_objs["Women's Fashion"],
                'name': 'Velvet Embroidered Evening Gown',
                'price': 2499.00,
                'original_price': 4999.00,
                'stock': 15,
                'rating': 4.9,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1566174053879-31528523f8ae?auto=format&fit=crop&w=800&q=80',
                'description': 'Stunning royal velvet evening gown with delicate sequin embellishments.'
            },
            {
                'category': category_objs["Women's Fashion"],
                'name': 'Women\'s Tailored Office Blazer',
                'price': 2999.00,
                'original_price': 5499.00,
                'stock': 20,
                'rating': 4.7,
                'is_featured': False,
                'image_url': 'https://images.unsplash.com/photo-1483985988355-763728e1935b?auto=format&fit=crop&w=800&q=80',
                'description': 'Crisp double-breasted formal blazer designed for modern professional women.'
            },

            # MEN'S FASHION
            {
                'category': category_objs["Men's Fashion"],
                'name': 'Men\'s Casual Linen Button-Down Shirt',
                'price': 1499.00,
                'original_price': 2499.00,
                'stock': 35,
                'rating': 4.6,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1596755094514-f87e34085b2c?auto=format&fit=crop&w=800&q=80',
                'description': 'Airy 100% organic linen casual shirt featuring a spread collar and chest pocket. Tailored for effortless summer style.'
            },
            {
                'category': category_objs["Men's Fashion"],
                'name': 'Classic Oxford Cotton Formal Shirt',
                'price': 1699.00,
                'original_price': 2999.00,
                'stock': 25,
                'rating': 4.8,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1602810318383-e386cc2a3ccf?auto=format&fit=crop&w=800&q=80',
                'description': 'Crisp Oxford cotton formal shirt designed with a button-down collar and wrinkle-resistant fabric.'
            },
            {
                'category': category_objs["Men's Fashion"],
                'name': 'Men\'s Classic Genuine Biker Leather Jacket',
                'price': 4999.00,
                'original_price': 8999.00,
                'stock': 10,
                'rating': 4.9,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1551028719-00167b16eac5?auto=format&fit=crop&w=800&q=80',
                'description': 'Rugged lambskin biker leather jacket with asymmetric zipper closure and quilted shoulder padding.'
            },

            # TOPS
            {
                'category': category_objs['Tops'],
                'name': 'Elegant Satin Button-Up Blouse',
                'price': 1199.00,
                'original_price': 1999.00,
                'stock': 30,
                'rating': 4.7,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1604014237800-1c9102c219da?auto=format&fit=crop&w=800&q=80',
                'description': 'Smooth silk-satin top with cuff sleeves for office wear and evening outings.'
            },
            {
                'category': category_objs['Tops'],
                'name': 'Essential Organic Cotton Crewneck T-Shirt',
                'price': 599.00,
                'original_price': 999.00,
                'stock': 50,
                'rating': 4.5,
                'is_featured': False,
                'image_url': 'https://images.unsplash.com/photo-1521572267360-ee0c2909d518?auto=format&fit=crop&w=800&q=80',
                'description': 'Ultra-soft combed organic cotton t-shirt with a pre-shrunk fit and durable ribbed crew collar.'
            },
            {
                'category': category_objs['Tops'],
                'name': 'Ribbed Knit Summer Crop Top',
                'price': 699.00,
                'original_price': 1299.00,
                'stock': 40,
                'rating': 4.6,
                'is_featured': False,
                'image_url': 'https://images.unsplash.com/photo-1503342217505-b0a15ec3261c?auto=format&fit=crop&w=800&q=80',
                'description': 'Stretch ribbed cotton crop top available in vibrant everyday pastel shades.'
            },

            # JEANS
            {
                'category': category_objs['Jeans'],
                'name': 'High-Waisted Slim Fit Blue Denim Jeans',
                'price': 1699.00,
                'original_price': 2999.00,
                'stock': 28,
                'rating': 4.6,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1541099649105-f69ad21f3246?auto=format&fit=crop&w=800&q=80',
                'description': 'Flattering high-rise denim jeans with optimal stretch and durable double-stitched seams.'
            },
            {
                'category': category_objs['Jeans'],
                'name': 'Men\'s Slim Fit Stretch Denim Jeans',
                'price': 1899.00,
                'original_price': 3299.00,
                'stock': 25,
                'rating': 4.7,
                'is_featured': False,
                'image_url': 'https://images.unsplash.com/photo-1542272604-780c96856552?auto=format&fit=crop&w=800&q=80',
                'description': 'Modern slim-fit jeans constructed from premium indigo denim with comfort-stretch technology.'
            },
            {
                'category': category_objs['Jeans'],
                'name': 'Women\'s Wide-Leg Vintage Flared Jeans',
                'price': 1899.00,
                'original_price': 3299.00,
                'stock': 20,
                'rating': 4.8,
                'is_featured': False,
                'image_url': 'https://images.unsplash.com/photo-1582552938357-32b906df40cb?auto=format&fit=crop&w=800&q=80',
                'description': 'Retro-inspired wide leg jeans with faded wash detailing.'
            },

            # KIDS
            {
                'category': category_objs['Kids'],
                'name': 'Kids Printed Cotton T-Shirt & Shorts Set',
                'price': 799.00,
                'original_price': 1399.00,
                'stock': 35,
                'rating': 4.6,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1519238263530-99bdd11df2ea?auto=format&fit=crop&w=800&q=80',
                'description': 'Soft and breathable 100% cotton printed shirt and shorts combo set for kids.'
            },
            {
                'category': category_objs['Kids'],
                'name': 'Girls Floral Party Frock Dress',
                'price': 1199.00,
                'original_price': 2199.00,
                'stock': 25,
                'rating': 4.8,
                'is_featured': False,
                'image_url': 'https://images.unsplash.com/photo-1622290291468-a28f7a7dc6a8?auto=format&fit=crop&w=800&q=80',
                'description': 'Charming layered floral frock dress with ribbon waist bow.'
            },
            {
                'category': category_objs['Kids'],
                'name': 'Boys Traditional Silk Kurta Pyjama Set',
                'price': 999.00,
                'original_price': 1899.00,
                'stock': 30,
                'rating': 4.7,
                'is_featured': False,
                'image_url': 'https://images.unsplash.com/photo-1503944583220-79d8926ad5e2?auto=format&fit=crop&w=800&q=80',
                'description': 'Festive silk blend ethnic kurta pyjama set for boys.'
            },

            # FOOTWEAR
            {
                'category': category_objs['Footwear'],
                'name': 'Minimalist Urban White Sneakers',
                'price': 1999.00,
                'original_price': 3499.00,
                'stock': 28,
                'rating': 4.7,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1549298916-b41d501d3772?auto=format&fit=crop&w=800&q=80',
                'description': 'Versatile low-top leather sneakers with cushioned insoles and durable anti-slip rubber outsole.'
            },
            {
                'category': category_objs['Footwear'],
                'name': 'Women\'s Elegant Strap Heel Sandals',
                'price': 2299.00,
                'original_price': 3999.00,
                'stock': 18,
                'rating': 4.6,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1543163521-1bf539c55dd2?auto=format&fit=crop&w=800&q=80',
                'description': 'Chic ankle strap high heels designed for evening wear and special celebrations.'
            },
            {
                'category': category_objs['Footwear'],
                'name': 'Classic Men\'s Leather Loafers',
                'price': 2799.00,
                'original_price': 4999.00,
                'stock': 20,
                'rating': 4.8,
                'is_featured': False,
                'image_url': 'https://images.unsplash.com/photo-1614252235316-8c857d38b5f4?auto=format&fit=crop&w=800&q=80',
                'description': 'Handcrafted genuine leather slip-on loafers for formal and smart-casual attire.'
            },
            {
                'category': category_objs['Footwear'],
                'name': 'Women\'s Handcrafted Ethnic Mojari Juttis',
                'price': 1299.00,
                'original_price': 2299.00,
                'stock': 30,
                'rating': 4.7,
                'is_featured': False,
                'image_url': 'https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?auto=format&fit=crop&w=800&q=80',
                'description': 'Embroidered Punjabi juttis with soft leather sole for festive wear.'
            },

            # HANDBAGS
            {
                'category': category_objs['Handbags'],
                'name': 'Elegance Genuine Leather Shoulder Tote Bag',
                'price': 2499.00,
                'original_price': 4499.00,
                'stock': 15,
                'rating': 4.9,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1584917865442-de89df76afd3?auto=format&fit=crop&w=800&q=80',
                'description': 'Spacious handcrafted leather tote handbag with multi-zip compartments and detachable shoulder strap.'
            },
            {
                'category': category_objs['Handbags'],
                'name': 'Women\'s Quilted Crossbody Chain Sling Bag',
                'price': 1799.00,
                'original_price': 3199.00,
                'stock': 22,
                'rating': 4.8,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1566150905458-1bf1fc113f0d?auto=format&fit=crop&w=800&q=80',
                'description': 'Elegant quilted faux leather sling bag with gold-tone chain strap.'
            },
            {
                'category': category_objs['Handbags'],
                'name': 'Designer Evening Metallic Clutch Bag',
                'price': 1499.00,
                'original_price': 2699.00,
                'stock': 18,
                'rating': 4.6,
                'is_featured': False,
                'image_url': 'https://images.unsplash.com/photo-1548036328-c9fa89d128fa?auto=format&fit=crop&w=800&q=80',
                'description': 'Shimmering metallic clutch bag with magnetic lock for parties.'
            },

            # JEWELLERY
            {
                'category': category_objs['Jewellery'],
                'name': 'Gold Plated Minimalist Pendant Necklace',
                'price': 999.00,
                'original_price': 1999.00,
                'stock': 35,
                'rating': 4.8,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?auto=format&fit=crop&w=800&q=80',
                'description': '18k gold plated dainty pendant necklace crafted from hypoallergenic brass.'
            },
            {
                'category': category_objs['Jewellery'],
                'name': 'Crystal Chandelier Drop Earrings',
                'price': 799.00,
                'original_price': 1499.00,
                'stock': 30,
                'rating': 4.7,
                'is_featured': False,
                'image_url': 'https://images.unsplash.com/photo-1630019852942-f89202989a59?auto=format&fit=crop&w=800&q=80',
                'description': 'Sparkling cubic zirconia crystal drop earrings for weddings and galas.'
            },
            {
                'category': category_objs['Jewellery'],
                'name': 'Traditional Kundan Pearl Choker Set',
                'price': 2999.00,
                'original_price': 5999.00,
                'stock': 12,
                'rating': 4.9,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1611591475777-233cd732222e?auto=format&fit=crop&w=800&q=80',
                'description': 'Royal Kundan necklace choker set with pearl drops and matching earrings.'
            },

            # ACCESSORIES
            {
                'category': category_objs['Accessories'],
                'name': 'Polarized UV400 Classic Aviator Sunglasses',
                'price': 1199.00,
                'original_price': 2199.00,
                'stock': 40,
                'rating': 4.7,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1572635196237-14b3f281503f?auto=format&fit=crop&w=800&q=80',
                'description': 'Lightweight metal frame aviator sunglasses featuring HD glare-blocking polarized lenses.'
            },
            {
                'category': category_objs['Accessories'],
                'name': 'Minimalist Steel Chronograph Wrist Watch',
                'price': 3499.00,
                'original_price': 6999.00,
                'stock': 20,
                'rating': 4.8,
                'is_featured': True,
                'image_url': 'https://images.unsplash.com/photo-1524805444758-089113d48a6d?auto=format&fit=crop&w=800&q=80',
                'description': 'Sleek stainless steel wrist watch with Japanese quartz movement and scratch-resistant glass.'
            },
            {
                'category': category_objs['Accessories'],
                'name': 'Genuine Bifold Leather Wallet for Men',
                'price': 999.00,
                'original_price': 1799.00,
                'stock': 35,
                'rating': 4.6,
                'is_featured': False,
                'image_url': 'https://images.unsplash.com/photo-1627123424574-724758594e93?auto=format&fit=crop&w=800&q=80',
                'description': 'Handcrafted slim leather wallet with RFID blocking protection.'
            }
        ]

        # Clear existing items and re-seed
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

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {len(products_data)} products in Rupees across {len(categories_data)} categories!'))
