from django.contrib import admin
from .models import Product , Message


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)


admin.site.site_header = "Ko`kchoy Adminstration"
admin.site.site_title = "Ko`kchoy Admin Portal"
admin.site.index_title = "Ko`kchoy Admin Panel"

admin.site.register(Message)