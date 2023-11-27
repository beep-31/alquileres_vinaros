from django.contrib import admin
from .models import Product, ProductImage, UserContact, Availability, ProductSell, ProductSellImage

# Register your models here
class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

class ProductSellImageAdmin(admin.StackedInline):
    model = ProductSellImage

class ProductAvailabilityAdmin(admin.StackedInline):
    model = Availability

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin, ProductAvailabilityAdmin]
    search_fields = ("title_ru",)

    class Meta:
        model = Product

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductSell)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductSellImageAdmin]
    search_fields = ("title_ru",)
    class Meta:
        model = Product

@admin.register(ProductSellImage)
class ProductSellImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Availability)
class ProductAvailabilityAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserContact)