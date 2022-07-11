from django.contrib import admin
from .models import Category, Product , Brand, ProductImages

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductImages)
