from django.contrib import admin

from .models import Category, Product

admin.site.site_header = 'E-commerce'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'slug',
                    'price', 'image', 'thumbnail', 'date_added')
    search_fields = ('name',)
    list_filter = (
        'category__name', 'price', 'date_added'
    )

