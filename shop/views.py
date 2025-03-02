from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from shop.models import Product, Category, Comment
from shop.forms import ProductForm, ProductModelForm


# Create your views here.


def index(request, category_id: int | None = None):
    search_query = request.GET.get('q', '')
    categories = Category.objects.all()

    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all().order_by('-updated_at')  # select * from products order by updated_at DESC
    if search_query:
        products = Product.objects.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'shop/home.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    categories = Category.objects.all()
    comments = Comment.objects.filter(product=product)

    context = {
        'product': product,
        'categories': categories,
        'comments': comments
    }
    return render(request, 'shop/detail.html', context)



# @login_required(login_url='/admin/')
# def product_create(request):
#     form = ProductModelForm()
#     if request.method == 'POST':
#         form = ProductModelForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#     context = {
#         'form': form
#     }
#     return render(request, 'shop/product-create.html', context)

@login_required(login_url='/admin/')
def product_create(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('index')

    context = {
        'form': form,
        'action': 'Create'
    }
    return render(request, 'shop/product-create.html', context)


@login_required(login_url='/admin/')
def product_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    form = ProductModelForm(instance=product)
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id)
    context = {
        'product': product,
        'form': form,
        'action': 'Update'
    }
    return render(request, 'shop/product-update.html', context)


@login_required(login_url='/admin/')
def product_delete(request, product_id):
    product = Product.objects.get(id=product_id)
    if product:
        product.delete()
        return redirect('index')
    return render(request, 'shop/detail.html', {'product': product})


def add_comment(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        name = request.POST.get("name")
        text = request.POST.get("text")

        if name and text:
            comment = Comment.objects.create(
                product=product,
                name=name,
                text=text
            )
            comment.save()

    return redirect("product_detail", product_id=product.id)


def comment_list_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    comments = Comment.objects.filter(product=product)

    return render(request, 'shop/detail.html', {'product': product, 'comments': comments})
