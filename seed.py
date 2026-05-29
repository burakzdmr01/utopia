import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'utopia.settings')
django.setup()

from products.models import Category, Product
from users.models import User

seller = User.objects.get(username='seller1')

laptops    = Category.objects.get(slug='laptops')
smartphones = Category.objects.get(slug='smartphones')
tvs        = Category.objects.get(slug='tvs')
tablets    = Category.objects.get(slug='tablets')
headphones = Category.objects.get(slug='headphones')
cameras    = Category.objects.get(slug='cameras')
monitors   = Category.objects.get(slug='monitors')
keyboards  = Category.objects.get(slug='keyboards')
mice       = Category.objects.get(slug='mice')
ram        = Category.objects.get(slug='ram')
storage    = Category.objects.get(slug='storage')
gpu        = Category.objects.get(slug='graphics-cards')
consoles   = Category.objects.get(slug='consoles')
gaming_laptops = Category.objects.get(slug='gaming-laptops')
routers    = Category.objects.get(slug='routers')
processors = Category.objects.get(slug='processors')
smart_watches = Category.objects.get(slug='smart-watches')

Product.objects.filter(slug='macbook-pro').update(category=laptops)
Product.objects.filter(slug='macbook-air-m2').update(category=laptops)
Product.objects.filter(slug='dell-xps-15').update(category=laptops)
Product.objects.filter(slug='hp-spectre-x360').update(category=laptops)
Product.objects.filter(slug='lenovo-thinkpad-x1').update(category=laptops)
Product.objects.filter(slug='iphone-15').update(category=smartphones)
Product.objects.filter(slug='samsung-galaxy-s24').update(category=smartphones)
Product.objects.filter(slug='google-pixel-8').update(category=smartphones)
Product.objects.filter(slug='samsung-4k-tv').update(category=tvs)
Product.objects.filter(slug='sony-bravia-55').update(category=tvs)
Product.objects.filter(slug='lg-oled-c3').update(category=tvs)

products = [
    ('iPad Pro M2', 'ipad-pro-m2', tablets, 1099.99, 15, '12.9 inch Liquid Retina, M2 chip'),
    ('Samsung Galaxy Tab S9', 'samsung-tab-s9', tablets, 799.99, 12, 'Snapdragon 8 Gen 2, 256GB'),
    ('Sony WH-1000XM5', 'sony-wh1000xm5', headphones, 349.99, 20, 'Industry-leading noise cancellation'),
    ('AirPods Pro 2', 'airpods-pro-2', headphones, 249.99, 30, 'Active noise cancellation, H2 chip'),
    ('Sony A7 IV', 'sony-a7-iv', cameras, 2499.99, 7, '33MP full-frame mirrorless camera'),
    ('Canon EOS R6', 'canon-eos-r6', cameras, 2199.99, 5, '20MP, 4K video, image stabilization'),
    ('LG UltraWide 34"', 'lg-ultrawide-34', monitors, 599.99, 8, '34 inch curved, 144Hz, WQHD'),
    ('Samsung Odyssey G7', 'samsung-odyssey-g7', monitors, 699.99, 6, '32 inch, 240Hz, 1ms response time'),
    ('Logitech MX Keys', 'logitech-mx-keys', keyboards, 119.99, 25, 'Wireless illuminated keyboard'),
    ('Logitech MX Master 3', 'logitech-mx-master-3', mice, 99.99, 40, 'Advanced wireless mouse, 4000 DPI'),
    ('Corsair Vengeance 32GB', 'corsair-vengeance-32gb', ram, 89.99, 35, 'DDR5 5600MHz, 2x16GB kit'),
    ('Samsung 990 Pro 1TB', 'samsung-990-pro-1tb', storage, 129.99, 30, 'NVMe SSD, 7450MB/s read speed'),
    ('RTX 4080 Super', 'rtx-4080-super', gpu, 999.99, 5, '16GB GDDR6X, ray tracing, DLSS 3'),
    ('RX 7900 XTX', 'rx-7900-xtx', gpu, 899.99, 4, '24GB GDDR6, AMD RDNA 3'),
    ('PlayStation 5', 'playstation-5', consoles, 499.99, 3, 'Next-gen gaming, 825GB SSD'),
    ('Xbox Series X', 'xbox-series-x', consoles, 499.99, 4, '4K gaming, 1TB SSD'),
    ('ASUS ROG Strix G16', 'asus-rog-strix-g16', gaming_laptops, 1799.99, 6, 'RTX 4070, i9, 32GB RAM, 165Hz'),
    ('MSI Raider GE78', 'msi-raider-ge78', gaming_laptops, 2199.99, 4, 'RTX 4080, i9, 64GB RAM'),
    ('TP-Link AX6000', 'tp-link-ax6000', routers, 299.99, 15, 'Wi-Fi 6, 8-stream, 6000Mbps'),
    ('Intel Core i9-14900K', 'intel-i9-14900k', processors, 589.99, 10, '24 cores, 6.0GHz boost, LGA1700'),
    ('AMD Ryzen 9 7950X', 'amd-ryzen-9-7950x', processors, 549.99, 8, '16 cores, 5.7GHz boost, AM5'),
    ('Apple Watch Series 9', 'apple-watch-s9', smart_watches, 399.99, 25, 'S9 chip, always-on display'),
    ('Samsung Galaxy Watch 6', 'samsung-galaxy-watch-6', smart_watches, 299.99, 20, '1.5 inch AMOLED, health tracking'),
]

for name, slug, category, price, stock, description in products:
    Product.objects.get_or_create(
        slug=slug,
        defaults=dict(name=name, category=category, seller=seller, price=price, stock=stock, description=description, is_active=True)
    )

print("Tamam!")
