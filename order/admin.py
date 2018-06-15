from django.contrib import admin
from order.models import Order


class JorneyInline(admin.TabularInline):
    model = Order.jorneys.through
    extra = 0
    model._meta.verbose_name_plural = ("Order Jorneys")

class OrderAdmin(admin.ModelAdmin):
    """Add items to Order in Admin"""
    inlines = [JorneyInline]
    list_filter = ('status',)
    search_fields = ('pk',)
    list_display = ('__str__', 'user', 'total', 'status',)
    exclude = ('jorneys',)


admin.site.register(Order, OrderAdmin)
