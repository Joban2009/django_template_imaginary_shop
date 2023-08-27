from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['Item', 'Price']

admin.site.register(Product, ProductAdmin)
admin.site.site_header = "Fruit Shop"
admin.site.site_title = "Fruit Shop Admin"
admin.site.index_title = "Welcome to Fruit Shop Portal"
