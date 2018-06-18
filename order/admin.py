from django.contrib import admin
from order.models import Order, OrderAnonim


class JourneyInline(admin.TabularInline):
    model = Order.journey
    extra = 0
    model._meta.verbose_name_plural = "Order Journeys"


class OrderAdmin(admin.ModelAdmin):
    """Add journeys in Admin"""
    inlines = [JourneyInline]
    search_fields = ('pk',)
    list_display = ('__str__', 'user', 'total',)


class OrderAnonimAdmin(admin.ModelAdmin):
    """Add journeys in Admin"""
    search_fields = ('pk',)
    list_display = ('__str__',)


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderAnonim, OrderAnonimAdmin)
