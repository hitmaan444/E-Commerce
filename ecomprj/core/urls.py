from django.urls import path
from core.views import index
from core import views
from core.views import category_list_view, product_detail_view, product_list_view, vendor_detail_view, vendor_list_view, index, product_list_category_view

app_name = "core"


urlpatterns = [
    
    #HOMEPAGE
    path("",index,name='index'),
    path("products/", views.product_list_view, name="product-list"),
    path("product/<pid>/", product_detail_view, name="product_detail"),
    
    
    
    path("category/", views.category_list_view, name="category-list"),
    path("category/<cid>", views.product_list_category_view, name="category-product-list"),
    path("vendors/", views.vendor_list_view, name="vendor-lists"),
    path("vendro/<vid>", views.vendor_detail_view, name="vendor-detail"),
    



]
