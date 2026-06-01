# ⚡ Utopia — Technology E-Commerce Platform

A full-featured technology e-commerce web application built with Django.
Inspired by stores like MediaMarkt, Vatan, and İtopya.

🌐 **Live Demo:** [https://utopia-1nz5.onrender.com](https://utopia-1nz5.onrender.com)

---

## 🚀 Features

- User authentication (login / signup / logout)
- Role-based access control (Admin, Seller, Customer)
- Product listing with search and category/subcategory filter
- Product detail page with customer reviews and star ratings
- Live currency converter (USD → EUR, GBP, TRY) via ExchangeRate-API
- Shopping cart and checkout system
- Order management and tracking
- Campaign / discount system with percentage-based pricing
- Physical shop locations page
- REST API with Django REST Framework
- Pagination (9 products per page)
- AJAX dynamic cart updates with toast notifications
- Responsive design with Bootstrap 5
- Admin panel with Jazzmin

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python 3.13, Django 6.0 |
| API | Django REST Framework |
| Frontend | Bootstrap 5, Bootstrap Icons |
| Database | SQLite |
| Admin | Jazzmin |
| Deployment | Render.com + Gunicorn + WhiteNoise |
| Third-party API | ExchangeRate-API |

---

## ⚙️ Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yourusername/utopia.git
cd utopia
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Collect static files:
```bash
python manage.py collectstatic
```

7. Run the server:
```bash
python manage.py runserver
```

8. Visit http://127.0.0.1:8000/

---

## 📡 API Endpoints

| Endpoint | Method | Auth | Description |
|----------|--------|------|-------------|
| /api/products/ | GET | No | List all products |
| /api/products/\<slug\>/ | GET | No | Product detail |
| /api/categories/ | GET | No | List categories |
| /api/campaigns/ | GET | No | List campaigns |
| /api/orders/ | GET | Yes | My orders |

---

## 🗄️ Models & Architecture

### Users App
- **User** — Extends Django's AbstractUser. Adds `role` field (admin/seller/customer), `phone`, and `avatar`. Role-based access controls what each user can do.

### Products App
- **Category** — Self-referential ForeignKey for parent/subcategory hierarchy. Supports unlimited nesting.
- **Product** — Belongs to a Category and a Seller. Has `price`, `discount` (percentage), `stock`, and `is_active` fields. Methods: `discounted_price()`, `is_on_sale()`.
- **Campaign** — ManyToMany relationship with Products. Has `discount` percentage, `start_date`, `end_date`, and `is_active`.

### Orders App
- **Cart** — OneToOne with User. Each user has one cart at a time.
- **CartItem** — ForeignKey to Cart and Product. Tracks quantity per item.
- **Order** — Created from cart on checkout. Has status choices: pending → confirmed → shipped → delivered → cancelled.
- **OrderItem** — Snapshot of product price at time of purchase to preserve historical pricing.

### Reviews App
- **Review** — ForeignKey to User and Product. `unique_together` constraint prevents duplicate reviews. Integer rating 1-5.

### Shops App
- **Shop** — Physical store locations with address, city, phone, email, working hours, and optional GPS coordinates.

### API App
- Serializers and ViewSets for Product, Category, Campaign, and Order models using Django REST Framework.

---

## 🏗️ Design Choices

- **Custom User Model** — Extended early to avoid migration issues later.
- **Subcategory System** — Self-referential FK on Category allows flexible hierarchy.
- **Discount on Product** — Stored as integer percentage; `discounted_price()` calculates final price at runtime.
- **OrderItem price snapshot** — Stores price at purchase time so future price changes don't affect old orders.
- **AJAX cart** — Uses Fetch API to add items without page reload, improving UX.
- **Third-party API** — ExchangeRate-API provides live currency rates with fallback static values if API is unavailable.
- **Django Forms** — Used for login and signup validation instead of raw POST data.

---

## 🧪 Testing

```bash
python manage.py test
```

17 tests across products, users, and orders apps covering:
- Page response codes
- Authentication flow
- Cart operations
- Model methods (discount calculation, string representation)

---

## 📦 Deployment

Deployed on **Render.com**:
- Gunicorn as WSGI server
- WhiteNoise for static file serving
- Auto-deploy from GitHub main branch
- SQLite database

---

## 👤 User Roles

| Role | Permissions |
|------|------------|
| Admin | Full access, admin panel |
| Seller | Can manage own products |
| Customer | Can browse, purchase, review |

---

## 📁 Project Structure

```
utopia/
├── api/          — REST API endpoints
├── orders/       — Cart, checkout, order management
├── products/     — Products, categories, campaigns
├── reviews/      — Product reviews
├── shops/        — Physical store locations
├── users/        — Authentication, profiles
├── templates/    — HTML templates
├── staticfiles/  — Collected static files
└── utopia/       — Project settings and URLs
```
