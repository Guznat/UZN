from django.contrib import admin
from .models import Product, Category, ExtraProductPicture

# Register your models here.
admin.site.register(Category)


class ExtraPictureInline(admin.TabularInline):
    fieldsets = [
        ('Upload Image', {'fields': ['extra_picture']})
    ]
    model = ExtraProductPicture
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'description', 'price', 'picture',
                           'category', 'extra_info', 'is_available',
                           'material', 'condition', 'amount', 'color', 'size']}),
    ]
    inlines = [ExtraPictureInline]


admin.site.register(Product, ProductAdmin)
