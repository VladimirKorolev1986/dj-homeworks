from django.contrib import admin

from logistic.models import StockProduct, Stock


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['address']


@admin.register(StockProduct)
class StockProductAdmin(admin.ModelAdmin):
    list_display = ['stock', 'product', 'quantity', 'price']
