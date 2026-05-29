import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'utopia.settings')
django.setup()

from products.models import Category, Product
from users.models import User

seller = User.objects.get(username='seller1')

def get(slug):
    return Category.objects.get(slug=slug)

products = [
    # Phones (ana kategori - eskiden vardı)
    ('Samsung Galaxy A54', 'samsung-galaxy-a54', get('smartphones'), 449.99, 30, 'Samsung Galaxy A54 5G, 6.4 inch Super AMOLED, 128GB storage, 5000mAh battery. Great mid-range smartphone with excellent camera system.'),
    ('Xiaomi 14 Pro', 'xiaomi-14-pro', get('smartphones'), 799.99, 20, 'Xiaomi 14 Pro with Snapdragon 8 Gen 3, 50MP Leica camera, 120Hz AMOLED display, 4880mAh with 120W fast charging.'),
    ('OnePlus 12', 'oneplus-12', get('smartphones'), 699.99, 15, 'OnePlus 12 with Snapdragon 8 Gen 3, Hasselblad camera, 5400mAh battery, 100W SUPERVOOC charging.'),

    # Network - Switches
    ('Cisco SG350-28', 'cisco-sg350-28', get('switches'), 349.99, 8, 'Cisco SG350-28 28-port Gigabit Managed Switch. Ideal for small businesses requiring reliable network infrastructure.'),
    ('TP-Link TL-SG108', 'tp-link-tl-sg108', get('switches'), 29.99, 50, 'TP-Link 8-Port Gigabit Desktop Switch, unmanaged, plug and play, energy efficient.'),
    ('Netgear GS308', 'netgear-gs308', get('switches'), 39.99, 40, 'NETGEAR 8-Port Gigabit Ethernet Unmanaged Switch, desktop or wall mount.'),

    # Network - Modems
    ('ASUS DSL-AC88U', 'asus-dsl-ac88u', get('modems'), 199.99, 10, 'ASUS DSL-AC88U ADSL/VDSL modem router, AC3100 dual-band Wi-Fi, AiMesh support.'),
    ('TP-Link TD-W9970', 'tp-link-td-w9970', get('modems'), 79.99, 20, 'TP-Link TD-W9970 300Mbps wireless N USB ADSL2+ modem router, 4 LAN ports.'),

    # Network - Access Points
    ('Ubiquiti UniFi AP', 'ubiquiti-unifi-ap', get('access-points'), 149.99, 15, 'Ubiquiti UniFi AP AC Lite, 802.11ac dual-band, up to 1167Mbps, PoE powered, indoor access point.'),
    ('TP-Link EAP670', 'tp-link-eap670', get('access-points'), 89.99, 20, 'TP-Link EAP670 Wi-Fi 6 AX3000 ceiling mount access point, 2.4GHz + 5GHz, MU-MIMO.'),

    # Computers - Desktop PCs
    ('Apple Mac Mini M2', 'apple-mac-mini-m2', get('desktop-pcs'), 599.99, 12, 'Apple Mac Mini with M2 chip, 8GB RAM, 256GB SSD. Compact and powerful desktop for everyday computing.'),
    ('Dell OptiPlex 7010', 'dell-optiplex-7010', get('desktop-pcs'), 899.99, 8, 'Dell OptiPlex 7010 Desktop, Intel Core i7-13700, 16GB DDR5, 512GB SSD, Windows 11 Pro.'),
    ('HP EliteDesk 800 G9', 'hp-elitedesk-800-g9', get('desktop-pcs'), 999.99, 6, 'HP EliteDesk 800 G9 Mini PC, Intel i7-12700, 16GB RAM, 512GB SSD, enterprise-grade reliability.'),

    # Computers - All-in-One
    ('Apple iMac 24"', 'apple-imac-24', get('all-in-one'), 1299.99, 8, 'Apple iMac 24-inch with M3 chip, 4.5K Retina display, 8GB RAM, 256GB SSD, 7-core GPU.'),
    ('Dell Inspiron 27 AIO', 'dell-inspiron-27-aio', get('all-in-one'), 1099.99, 6, 'Dell Inspiron 27 7000 All-in-One, Intel i7, 16GB RAM, 512GB SSD, 27-inch FHD touch display.'),
    ('HP Envy 32 AIO', 'hp-envy-32-aio', get('all-in-one'), 1499.99, 4, 'HP ENVY 32 All-in-One, Intel i9, 32GB RAM, 1TB SSD, 32-inch 4K display with B&O audio.'),

    # Computers - Servers
    ('Dell PowerEdge T150', 'dell-poweredge-t150', get('servers'), 799.99, 4, 'Dell PowerEdge T150 Tower Server, Intel Xeon E-2300, 16GB ECC RAM, 2TB HDD, ideal for SMBs.'),
    ('HPE ProLiant ML30', 'hpe-proliant-ml30', get('servers'), 899.99, 3, 'HPE ProLiant ML30 Gen10 Plus Tower Server, Intel Xeon E-2300, 16GB DDR4, 1TB SATA.'),

    # Peripherals - Printers
    ('HP LaserJet Pro M404n', 'hp-laserjet-pro-m404n', get('printers'), 299.99, 10, 'HP LaserJet Pro M404n, 38ppm, 1200x1200 dpi, USB & Ethernet, duplex printing.'),
    ('Epson EcoTank ET-2850', 'epson-ecotank-et-2850', get('printers'), 249.99, 15, 'Epson EcoTank ET-2850 wireless all-in-one printer, supertank ink system, 3 years of ink included.'),
    ('Canon PIXMA TR8620', 'canon-pixma-tr8620', get('printers'), 179.99, 12, 'Canon PIXMA TR8620 all-in-one printer, wireless, auto duplex, 15 ipm black, 10 ipm color.'),

    # Peripherals - Scanners
    ('Fujitsu ScanSnap iX1600', 'fujitsu-scansnap-ix1600', get('scanners'), 449.99, 6, 'Fujitsu ScanSnap iX1600 document scanner, 40ppm, Wi-Fi, touchscreen, ADF 50 sheets.'),
    ('Epson Perfection V39', 'epson-perfection-v39', get('scanners'), 79.99, 15, 'Epson Perfection V39 flatbed scanner, 4800 dpi optical resolution, USB powered.'),

    # PC Components - Motherboards
    ('ASUS ROG Maximus Z790', 'asus-rog-maximus-z790', get('motherboards'), 599.99, 5, 'ASUS ROG Maximus Z790 Hero, DDR5, PCIe 5.0, Wi-Fi 6E, 5Gbps LAN, for Intel 12th/13th gen.'),
    ('MSI MAG B650 Tomahawk', 'msi-mag-b650-tomahawk', get('motherboards'), 229.99, 10, 'MSI MAG B650 TOMAHAWK WIFI, AMD AM5 socket, DDR5, PCIe 5.0, 2.5G LAN, Wi-Fi 6E.'),
    ('Gigabyte Z790 Aorus Elite', 'gigabyte-z790-aorus', get('motherboards'), 279.99, 8, 'Gigabyte Z790 AORUS Elite AX, DDR5, PCIe 5.0, Wi-Fi 6E, USB 3.2 Gen 2, Intel LGA1700.'),

    # PC Components - Power Supplies
    ('Corsair RM850x', 'corsair-rm850x', get('power-supplies'), 139.99, 15, 'Corsair RM850x 850W 80 Plus Gold fully modular ATX power supply, zero RPM fan mode.'),
    ('EVGA SuperNOVA 750 G6', 'evga-supernova-750-g6', get('power-supplies'), 119.99, 12, 'EVGA SuperNOVA 750 G6, 80 Plus Gold, fully modular, compact 140mm size.'),
    ('Seasonic Focus GX-1000', 'seasonic-focus-gx-1000', get('power-supplies'), 179.99, 8, 'Seasonic Focus GX-1000W 80 Plus Gold fully modular, ultra quiet, 10 year warranty.'),

    # PC Components - PC Cases
    ('Lian Li PC-O11 Dynamic', 'lian-li-o11-dynamic', get('pc-cases'), 149.99, 10, 'Lian Li PC-O11 Dynamic mid tower case, tempered glass, supports 360mm radiator, excellent airflow.'),
    ('NZXT H510', 'nzxt-h510', get('pc-cases'), 79.99, 15, 'NZXT H510 compact ATX mid tower case, tempered glass, cable management, 2x120mm fans included.'),
    ('Fractal Design Meshify 2', 'fractal-meshify-2', get('pc-cases'), 129.99, 8, 'Fractal Design Meshify 2 ATX mid tower, high airflow mesh front, modular interior.'),

    # PC Components - Cooling
    ('Noctua NH-D15', 'noctua-nh-d15', get('cooling'), 99.99, 12, 'Noctua NH-D15 dual tower CPU cooler, 2x140mm fans, supports Intel LGA1700 and AMD AM5.'),
    ('Corsair H150i Elite', 'corsair-h150i-elite', get('cooling'), 179.99, 8, 'Corsair iCUE H150i Elite Capellix 360mm liquid CPU cooler, RGB, zero RPM mode.'),
    ('be quiet! Dark Rock Pro 4', 'bequiet-dark-rock-pro-4', get('cooling'), 89.99, 10, 'be quiet! Dark Rock Pro 4 dual tower CPU cooler, 250W TDP, silent wings fans.'),

    # PC Accessories - Mousepads
    ('SteelSeries QcK XXL', 'steelseries-qck-xxl', get('mousepads'), 39.99, 30, 'SteelSeries QcK XXL gaming mousepad, 900x400mm, micro-textured cloth surface, anti-slip base.'),
    ('Logitech G840 XL', 'logitech-g840-xl', get('mousepads'), 49.99, 25, 'Logitech G840 XL gaming mousepad, 900x400x3mm, consistent surface for precise mouse control.'),

    # PC Accessories - USB Hubs
    ('Anker 10-Port USB Hub', 'anker-10-port-usb-hub', get('usb-hubs'), 49.99, 25, 'Anker 10-Port USB 3.0 hub with 60W power adapter, data transfer up to 5Gbps.'),
    ('CalDigit TS4 Thunderbolt', 'caldigit-ts4', get('usb-hubs'), 399.99, 8, 'CalDigit TS4 Thunderbolt 4 dock, 18 ports, 98W host charging, dual 6K display support.'),

    # PC Accessories - Cables
    ('Belkin USB-C to USB-C 2m', 'belkin-usbc-2m', get('cables'), 19.99, 50, 'Belkin USB-C to USB-C cable 2m, 100W fast charging, 480Mbps data transfer, braided nylon.'),
    ('Cable Matters HDMI 2.1', 'cable-matters-hdmi21', get('cables'), 14.99, 60, 'Cable Matters HDMI 2.1 cable 2m, 8K@60Hz, 4K@120Hz, 48Gbps bandwidth, HDR support.'),

    # PC Accessories - Webcams
    ('Logitech C920', 'logitech-c920', get('webcams'), 79.99, 30, 'Logitech C920 HD Pro Webcam, 1080p/30fps, stereo audio, autofocus, works with Zoom and Teams.'),
    ('Razer Kiyo Pro', 'razer-kiyo-pro', get('webcams'), 149.99, 15, 'Razer Kiyo Pro streaming webcam, 1080p/60fps, adaptive light sensor, uncompressed USB output.'),

    # Gaming - Controllers
    ('Xbox Wireless Controller', 'xbox-wireless-controller', get('controllers'), 59.99, 35, 'Xbox Wireless Controller, textured grip, Bluetooth, USB-C, compatible with Xbox and PC.'),
    ('PS5 DualSense', 'ps5-dualsense', get('controllers'), 69.99, 30, 'PlayStation 5 DualSense wireless controller, haptic feedback, adaptive triggers, built-in microphone.'),
    ('Nintendo Pro Controller', 'nintendo-pro-controller', get('controllers'), 69.99, 20, 'Nintendo Switch Pro Controller, Bluetooth, motion controls, HD rumble, 40 hour battery life.'),

    # Gaming - Gaming Chairs
    ('Secretlab Titan EVO', 'secretlab-titan-evo', get('gaming-chairs'), 449.99, 8, 'Secretlab TITAN Evo 2022 gaming chair, 4-way lumbar support, magnetic memory foam head pillow.'),
    ('DXRacer Formula F08', 'dxracer-formula-f08', get('gaming-chairs'), 299.99, 10, 'DXRacer Formula Series gaming chair, adjustable armrests, lumbar support, up to 200lbs.'),

    # Business Solutions
    ('Epson EB-L200F Projector', 'epson-eb-l200f', get('projectors'), 1299.99, 4, 'Epson EB-L200F laser projector, 4500 lumens, Full HD 1080p, HDMI, wireless, long lamp life.'),
    ('BenQ MH560 Projector', 'benq-mh560', get('projectors'), 499.99, 6, 'BenQ MH560 DLP projector, 3800 lumens, 1080p, HDMI, USB, 20000:1 contrast ratio.'),
    ('Logitech Rally Bar', 'logitech-rally-bar', get('video-conferencing'), 2999.99, 3, 'Logitech Rally Bar all-in-one video conferencing system, 4K camera, AI auto-framing.'),
    ('Poly Studio X50', 'poly-studio-x50', get('video-conferencing'), 1999.99, 4, 'Poly Studio X50 video bar, 4K camera, Zoom and Teams certified, NoiseBlockAI.'),
    ('APC Back-UPS 1500VA', 'apc-back-ups-1500va', get('ups'), 199.99, 15, 'APC Back-UPS 1500VA 865W UPS, 10 outlets, AVR, USB charging port, software included.'),
    ('CyberPower CP1500PFCLCD', 'cyberpower-cp1500', get('ups'), 229.99, 12, 'CyberPower CP1500PFCLCD 1500VA 1000W UPS, pure sine wave, LCD display, 12 outlets.'),

    # Software
    ('Microsoft Windows 11 Pro', 'windows-11-pro', get('operating-systems'), 199.99, 100, 'Microsoft Windows 11 Pro license key, 1 PC, lifetime activation, digital delivery.'),
    ('macOS Ventura Upgrade', 'macos-ventura', get('operating-systems'), 0.00, 100, 'macOS Ventura free upgrade for compatible Mac computers. Download from Apple App Store.'),
    ('Norton 360 Deluxe', 'norton-360-deluxe', get('antivirus'), 49.99, 100, 'Norton 360 Deluxe, 5 devices, 1 year, 50GB cloud backup, VPN, password manager.'),
    ('Kaspersky Total Security', 'kaspersky-total-security', get('antivirus'), 39.99, 100, 'Kaspersky Total Security, 3 devices, 1 year, antivirus, VPN, password manager, parental controls.'),
    ('Microsoft Office 365', 'microsoft-office-365', get('office-software'), 99.99, 100, 'Microsoft 365 Personal, 1 user, 1 year, Word, Excel, PowerPoint, 1TB OneDrive storage.'),
    ('Adobe Creative Cloud', 'adobe-creative-cloud', get('office-software'), 599.99, 100, 'Adobe Creative Cloud All Apps, 1 year, Photoshop, Illustrator, Premiere Pro, 100GB storage.'),
]

created = 0
skipped = 0
for name, slug, category, price, stock, description in products:
    obj, was_created = Product.objects.get_or_create(
        slug=slug,
        defaults=dict(name=name, category=category, seller=seller, price=price, stock=stock, description=description, is_active=True)
    )
    if was_created:
        created += 1
    else:
        skipped += 1

print(f"Oluşturuldu: {created}, Zaten vardı: {skipped}")
