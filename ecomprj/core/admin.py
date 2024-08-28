from django.contrib import admin
from core.models import Product,Category,Vendor,CartOrder,CartOrderItems,Wishlist,Address,ProductImages,ProductReview

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ["user", "title", "image", "price", "featured", "product_status", "vendor", "category", "pid", "date"]  # Corrected "product_status" to "products_status"

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "image"]

class VendorAdmin(admin.ModelAdmin):
    list_display = ["title", "image", "address", "description", "user", "contact", "address"]

class CartOrderAdmin(admin.ModelAdmin):
    list_display = ["user", "price", "paid_status", "order_date", "products_status"]  # Corrected "product_status" to "products_status"

class CartOrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "item", "image", "qty", "price", "total", "invoice_no"]  # Removed "invoice_no"

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "review", "rating"]

class WishlistAdmin(admin.ModelAdmin):
    list_display = ["user", "product"]

class AddressAdmin(admin.ModelAdmin):
    list_display = ["user", "address", "status"] 

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItems, CartOrderItemAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Address, AddressAdmin)
