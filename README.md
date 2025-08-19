
---

# Simple Shop

A lightweight Django e-commerce application for managing **products** and **categories**. Users can create, edit, and delete products and categories, assign products to categories, and view product details.

---

## Features

* **Products Management**

  * Create, edit, and delete products
  * Assign products to categories
  * Upload product images
  * Track stock items and prices

* **Categories Management**

  * Create, edit, and delete categories
  * Assign multiple products to a category
  * Upload category images

* **Relationships**

  * Many-to-many relationship between products and categories
  * Easy navigation between products and categories

* **Frontend**

  * Clean HTML templates
  * Forms for create/update actions
  * List and detail pages for products and categories

---

## Installation

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd simple_shop_project
```

2. **Create a virtual environment**

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create a superuser (optional)**

```bash
python manage.py createsuperuser
```

6. **Run the development server**

```bash
python manage.py runserver
```

---

## Usage

### Products

| URL                    | Description          | Screenshot                                        |
| ---------------------- | -------------------- | ------------------------------------------------- |
| `/products/`           | List all products    | ![Product List](docs/images/products_list.png)    |
| `/products/create/`    | Create a new product | ![Create Product](docs/images/product_create.png) |
| `/products/<id>/`      | View product details | ![Product Detail](docs/images/product_detail.png) |
| `/products/<id>/edit/` | Edit product         | ![Edit Product](docs/images/product_edit.png)     |

### Categories

| URL                      | Description                           | Screenshot                                          |
| ------------------------ | ------------------------------------- | --------------------------------------------------- |
| `/categories/`           | List all categories                   | ![Category List](docs/images/categories_list.png)   |
| `/categories/create/`    | Create a new category                 | ![Create Category](docs/images/category_create.png) |
| `/categories/<id>/`      | View category details                 | ![Category Detail](docs/images/category_detail.png) |
| `/categories/<id>/edit/` | Edit category, assign/remove products | ![Edit Category](docs/images/category_edit.png)     |

---

## Project Structure

```
simple_shop_project/
├── categories/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── templates/categories/
├── products/
│   ├── models.py
│   ├── views.py
│   └── templates/products/
├── simple_shop/
│   ├── settings.py
│   └── urls.py
└── manage.py
```

---
## ScreenShots

![1](docs/images/1.png)
![2](docs/images/2.png)
![3](docs/images/3.png)
![4](docs/images/4.png)
![5](docs/images/5.png)
![6](docs/images/6.png)
![7](docs/images/7.png)
![8](docs/images/8.png)

---

