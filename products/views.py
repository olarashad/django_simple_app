from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from django.http import HttpResponseNotAllowed
from .models import Product
from categories.models import Category  # نجيب الموديل بتاع الكاتيجوري

def list_products(request):
    products = Product.objects.all()
    return render(request, "products/list.html", {"products": products})

def show_product(request, pk: int):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/detail.html", {"product": product})

def create_product(request):
    error = None
    categories = Category.objects.all()  # هنبعت للـ template
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        price = request.POST.get("price", "0").strip()
        instock_items = request.POST.get("instock_items", "0").strip()
        code = request.POST.get("code", "").strip()
        description = request.POST.get("description", "").strip()
        image = request.FILES.get('image')
        category_id = request.POST.get("category")
        category = Category.objects.get(pk=category_id) if category_id else None

        if not name or not code:
            error = "Name and Code are required."
        else:
            try:
                price_val = round(float(price), 2)
                instock_val = int(instock_items)
                product = Product.objects.create(
                    name=name,
                    price=price_val,
                    instock_items=instock_val,
                    code=code,
                    description=description,
                    image=image,
                    category=category
                )
                return redirect("product_detail", pk=product.pk)
            except ValueError:
                error = "Price must be a number and stock must be an integer."
            except IntegrityError:
                error = "Code must be unique. This code already exists."

    return render(request, "products/form.html", {
        "error": error,
        "mode": "create",
        "categories": categories
    })

def edit_product(request, pk: int):
    product = get_object_or_404(Product, pk=pk)
    error = None
    categories = Category.objects.all()
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        price = request.POST.get("price", "0").strip()
        instock_items = request.POST.get("instock_items", "0").strip()
        code = request.POST.get("code", "").strip()
        description = request.POST.get("description", "").strip()
        image = request.FILES.get('image')
        category_id = request.POST.get("category")
        category = Category.objects.get(pk=category_id) if category_id else None

        if image:
            product.image = image
        if not name or not code:
            error = "Name and Code are required."
        else:
            try:
                product.name = name
                product.price = round(float(price), 2)
                product.instock_items = int(instock_items)
                product.code = code
                product.description = description
                product.category = category
                product.save()
                return redirect("product_detail", pk=product.pk)
            except ValueError:
                error = "Price must be a number and stock must be an integer."
            except IntegrityError:
                error = "Code must be unique. This code already exists."

    return render(request, "products/form.html", {
        "error": error,
        "mode": "edit",
        "product": product,
        "categories": categories
    })

def delete_product(request, pk: int):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect("product_list")
    if request.method == "GET":
        return render(request, "products/confirm_delete.html", {"product": product})
    return HttpResponseNotAllowed(["GET", "POST"])
