from django.contrib import admin
from .models import Product, Order
# Register your models here.
class OrderInLine(admin.TabularInline):
    model = Order.products.through


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        OrderInLine,
    ]
    list_display = 'pk', 'name', 'short_dis', 'price', 'discount'
    list_display_links = 'pk', 'name'
    ordering = 'pk',
    search_fields = 'name', 'description'
    fieldsets = [
        (None, {
            fields
        })
    ]
    def short_dis(self, obj: Product) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + '.....'

class ProductInLine(admin.StackedInline):
    model = Order.products.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ProductInLine,
    ]
    list_display = 'delivery_address', 'promocode', 'created_at', 'user_verbase'

    def get_queryset(self, request):
        return Order.objects.select_related('user').prefetch_related('products')

    def user_verbase(self, obj: Order) -> str:
        return obj.user.first_name or obj.user.username
# admin.site.register(Product, ProductAdmin)