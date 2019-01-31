import random
from django.contrib import admin
from product.models import Journey, Category, JourneyPhoto, Comment


class JourneyPhotoInline(admin.TabularInline):
    model = JourneyPhoto
    extra = 0


class JourneyAdmin(admin.ModelAdmin):
    """Add photos to Journey in Admin"""
    inlines = [JourneyPhotoInline]
    list_display = ('sku', '__str__', 'category',)
    list_filter = ('category',)
    search_fields = ('sku',)
    readonly_fields = ('sku',)

    def save_model(self, request, obj, form, change):
        """Add SKU to Journey."""
        super().save_model(request, obj, form, change)
        if not obj.sku:
            obj.sku = str(obj.id) + str(random.randint(100, 999))
            obj.save()


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name_uk', 'slug',)
    search_fields = ('name_uk',)


admin.site.register(Journey, JourneyAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment)
