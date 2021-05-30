from django.contrib import admin

# Register your models here.

from .models import MeasureUnit, Category, Product, Buy

admin.site.register(MeasureUnit)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Buy)
