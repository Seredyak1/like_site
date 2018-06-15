import random
from django.contrib import admin
from product.models import Jorney, Category, JorneyPhoto

class JorneyPhotoInline(admin.TabularInline):
    model = JorneyPhoto
    extra = 0


class JorneyAdmin(admin.ModelAdmin):
    """Add photos to Item in Admin"""
    inlines = [JorneyPhotoInline]
    list_display = ('sku', '__str__', 'category',)
    list_filter = ('category',)
    search_fields = ('sku',)
    readonly_fields = ('sku',)

    def save_model(self, request, obj, form, change):
        """Add SKU to Item."""
        super().save_model(request, obj, form, change)
        if not obj.sku:
            obj.sku = str(obj.id) + str(random.randint(100, 999))
            obj.save()


admin.site.register(Jorney, JorneyAdmin)
admin.site.register(Category)
