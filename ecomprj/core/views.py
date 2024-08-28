from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count
from core.models import Product,Category,Vendor,CartOrder,CartOrderItems,Wishlist,Address,ProductImages,ProductReview


def index(request):
    product = Product.objects.all().order_by("-id")
    
    context = {
        "products":product
    }
    return render(request, "core/index.html", context)



def product_list_view(request):
    products = Product.objects.filter(product_status="published").order_by("-id")
    # product = Product.objects.all().order_by("-id")
    # vendor = Vendor.objects.get(vid=vid)
    
    context = {
        "products":products,
        # "vendor":vendor
    }
    
    return render(request, "core/product-list.html", context)



def category_list_view(request):
    categories = Category.objects.all()
    
    
    context = {
        "categories":categories
    }
    
    return render (request, "core/category-list.html", context)



def product_list_category_view(request, cid):
    
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status="published", category=category)
    
    context = {
        "category":category,
        "products":products,
        
    }
    
    
    return render (request, "core/category-product-list.html", context)



def vendor_list_view(request):
    vendors = Vendor.objects.annotate(num_products=Count('product')).order_by("-id")
    
    context = {
        "vendors": vendors
    }
    
    return render (request, "core/vendor-list.html", context)



def vendor_detail_view(request,vid):
    
    vendor = Vendor.objects.get(vid=vid)
    products = Product.objects.filter(vendor=vendor, product_status="published")
    
    context = {
        "vendor":vendor,
        "products":products
        
    }

    return render(request, "core/vendor-detail.html", context)


def product_detail_view(request, pid):
    product = Product.objects.get(pid=pid)
    
    
    context = {
        "product":product,
    }
    
    return render(request, "core/product-detail.html", context)


    


