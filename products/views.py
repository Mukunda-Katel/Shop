from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Avg
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Product, Category, ProductLike
from reviews.models import Review
from .forms import ProductForm

def home(request):
    products = Product.objects.filter(available=True).order_by('-created_at')[:8]
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'products/home.html', context)

def product_list(request):
    query = request.GET.get('q')
    category_id = request.GET.get('category')
    
    products = Product.objects.filter(available=True)
    
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(seller__username__icontains=query)
        )
    
    if category_id:
        products = products.filter(category_id=category_id)
    
    products = products.order_by('-created_at')
    
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    categories = Category.objects.all()
    
    context = {
        'page_obj': page_obj,
        'categories': categories,
        'query': query,
        'selected_category': int(category_id) if category_id else None,
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk, available=True)
    reviews = Review.objects.filter(product=product)
    avg_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    
    user_has_liked = False
    if request.user.is_authenticated:
        user_has_liked = ProductLike.objects.filter(
            user=request.user, product=product
        ).exists()
    
    context = {
        'product': product,
        'reviews': reviews,
        'avg_rating': avg_rating,
        'user_has_liked': user_has_liked,
        'total_likes': ProductLike.objects.filter(product=product).count(),
    }
    return render(request, 'products/product_detail.html', context)

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            messages.success(request, 'Product created successfully!')
            return redirect('products:detail', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})

@login_required
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk, seller=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('products:detail', pk=product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form, 'product': product})

@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk, seller=request.user)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('products:list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})

@login_required
def toggle_like(request, pk):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=pk)
        like, created = ProductLike.objects.get_or_create(
            user=request.user, product=product
        )
        if not created:
            like.delete()
            liked = False
        else:
            liked = True
        
        total_likes = ProductLike.objects.filter(product=product).count()
        
        return JsonResponse({
            'liked': liked,
            'total_likes': total_likes
        })
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

def my_products(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')
    
    products = Product.objects.filter(seller=request.user).order_by('-created_at')
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'products/my_products.html', {'page_obj': page_obj})
