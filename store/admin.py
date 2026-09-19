from django.contrib import admin
from .models import Category, Product, Order, OrderItem

admin.site.site_header = "Fashion Store Admin Portal"
admin.site.site_title = "Fashion Store Management"
admin.site.index_title = "Manage Catalog, Orders & Inventory"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'original_price', 'stock', 'rating', 'is_featured', 'created_at']
    list_filter = ['category', 'is_featured', 'stock']
    list_editable = ['price', 'original_price', 'stock', 'is_featured']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'full_name', 'email', 'total_amount', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['full_name', 'email', 'id']
    inlines = [OrderItemInline]
