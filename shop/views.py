from django.shortcuts import render, get_object_or_404

from shop.models import Product, Category


# Create your views here.


def index(request):
    categories = Category.objects.all()
    products = Product.objects.all().order_by('-updated_at')  # select * from products order by updated_at DESC
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/home.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product
    }
    return render(request, 'shop/detail.html', context)


def category_products(request, category_id):
    categories = Category.objects.all()
    selected_category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=selected_category)

    return render(request, 'shop/home.html', {
        'categories': categories,
        'products': products,
        'selected_category': selected_category
    })
