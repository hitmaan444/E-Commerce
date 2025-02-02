from django.db import models
from shortuuid.django_fields import ShortUUIDField 
from django.utils.html import mark_safe
from userauths.models import User
from email.policy import default
from pyexpat import model
from unicodedata import decimal

STATUS_CHOICES = (
    ("processing", "Processing"),
    ("shipped", "Shipped"),
    ("delivered", "Delivered"),
)

STATUS = (
    ("draft", "Draft"),
    ("disabled", "Disabled"),
    ("rejected", "Rejected"),
    ("in_review", "In Review"),
    ("published", "Published"),
)


RATING = (
    (1, "⭑☆☆☆☆"),
    (2, "⭑⭑☆☆☆"),
    (3, "⭑⭑⭑☆☆"),
    (4, "⭑⭑⭑⭑☆"),
    (5, "⭑⭑⭑⭑⭑"),
)


class Category(models.Model):
    # cid = models.UUIDField(unique=True, max_length=20, prefix="cat", alphabet="abcdefghijklm12345")
    
    cid = ShortUUIDField(unique=True, max_length=30, prefix="cat", alphabet="abcdefghijklm12345")
    title = models.CharField(max_length=100, default="food")
    image = models.ImageField(upload_to="category", default="category.jpg")
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % self.image.url)

    def __str__(self):
        return self.title


class Tags(models.Model):
    pass

class Vendor(models.Model):
    vid = ShortUUIDField(unique=True, max_length=30, prefix="ven", alphabet="abcdefghijklm12345")
    title = models.CharField(max_length=100, default="nestify")
    image = models.ImageField(upload_to="vendor", default="vendor.jpg")
    description = models.TextField(null=True, blank=True, default="I am an amazing vendor")
    address = models.CharField(max_length=100, default="123 Main street")
    contact = models.CharField(max_length=100, default="123 (456) 789")
    chat_resp_time = models.CharField(max_length=100, default="100")
    shipping_on_time = models.CharField(max_length=100, default="100")
    authenticate_rating = models.CharField(max_length=100, default="1")
    days_return = models.CharField(max_length=100, default="1")
    warranty_period = models.CharField(max_length=100, default="1")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Vendors"

    def vendor_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % self.image.url)

    def __str__(self):
        return self.title


class Product(models.Model):
    pid = ShortUUIDField(unique=True, max_length=5, alphabet="abc12")
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category", default="product.jpg")
    description = models.TextField(null=True, blank=True, default="fresh pear")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, related_name="product")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=1.99)
    old_price = models.DecimalField(max_digits=12, decimal_places=2, default=2.99)
    specifications = models.TextField(null=True, blank=True)
    # tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)
    product_status = models.CharField(choices=STATUS, max_length=10, default="in_review")
    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)
    sku = ShortUUIDField(unique=True, max_length=40, prefix="sku", alphabet="1234567890")
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Products"

    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % self.image.url)

    def __str__(self):
        return self.title
    
    def __str__(self):
        return self.pid

    def get_percentage(self):
        new_price = ((self.old_price - self.price) / self.old_price) * 100
        return new_price


class ProductImages(models.Model):
    images = models.ImageField(upload_to="productimages", default="product.jpg")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Images"


class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=1.99)
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    products_status = models.CharField(choices=STATUS_CHOICES, max_length=30, default="processing")

    class Meta:
        verbose_name_plural = "Cart Orders"


class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=200) 
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.ImageField(upload_to="cartorderitems", default="product.jpg")
    qty = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=1.99)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=1.99)

    class Meta:
        verbose_name_plural = "Cart Order Items"

    def order_img(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image,))


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=1)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Reviews"

    def __str__(self):
        return self.product.title

    def get_rating(self):
        return self.rating


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Wishlist"

    def get_rating(self):
        return self.rating


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Addresses"