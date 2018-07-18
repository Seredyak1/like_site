from django.contrib import admin

from order.models import Order, OrderAnonim

class OrderAnonimAdmin(admin.ModelAdmin):
    list_display = ('name', 'contacted',)
    list_filter = ('contacted',)

admin.site.register(Order)
admin.site.register(OrderAnonim, OrderAnonimAdmin)
